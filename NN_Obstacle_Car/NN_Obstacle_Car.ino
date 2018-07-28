#include <Servo.h>  //servo library
Servo myservo;      // create servo object to control servo

int Echo = A4;  
int Trig = A5; 
#define ENA 5
#define ENB 6
#define IN1 7
#define IN2 8
#define IN3 9
#define IN4 11

/******************************************************************
   Network Configuration
 ******************************************************************/
const int InputNodes = 3; // incluye neurona de BIAS
const int HiddenNodes = 4; //incluye neurona de BIAS
const int OutputNodes = 4;
int i, j;
double Accum;
double Hidden[HiddenNodes];
double Output[OutputNodes];
float HiddenWeights[3][4] = {{1.8991509504079183, -0.4769472541445052, -0.6483690220539764, -0.38609165249078925}, {-0.2818610915467527, 4.040695699457223, 3.2291858058243843, -2.894301104732614}, {0.3340650864625773, -1.4016114422346901, 1.3580053902963762, -0.981415976256285}};
float OutputWeights[4][4] = {{1.136072297461121, 1.54602394937381, 1.6194612259569254, 1.8819066696635067}, {-1.546966506764457, 1.3951930739494225, 0.19393826092602756, 0.30992504138547006}, {-0.7755982417649826, 0.9390808625728915, 2.0862510744685485, -1.1229484266101883}, {-1.2357090352280826, 0.8583930286034466, 0.724702079881947, 0.9762852709700459}};
/******************************************************************
   End Network Configuration
 ******************************************************************/

void stop() {
  digitalWrite(ENA, LOW); //Desactivamos los motores
  digitalWrite(ENB, LOW); //Desactivamos los motores
  Serial.println("Stop!");
} 

//Medir distancia en Centimetros
int Distance_test() {
  digitalWrite(Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(20);
  digitalWrite(Trig, LOW);
  float Fdistance = pulseIn(Echo, HIGH);
  Fdistance= Fdistance / 58;
  return (int)Fdistance;
}

void setup() {
  myservo.attach(3);  // attach servo on pin 3 to servo object
  Serial.begin(9600);
  pinMode(Echo, INPUT);
  pinMode(Trig, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);
  stop();
  myservo.write(90);  //posicion inicial en el centro
  delay(500); 
} 

unsigned long previousMillis = 0;   // para medir ciclos de tiempo
const long interval = 25;           // intervalos cada x milisegundos
int grados_servo = 90;                // posicion del servo que mueve el sensor ultrasonico
bool clockwise = true;              // sentido de giro del servo
const long ANGULO_MIN = 30; 
const long ANGULO_MAX = 150; 
double ditanciaMaxima = 50.0;       // distancia de lejania desde la que empieza a actuar la NN
int incrementos = 9;                // incrementos por ciclo de posicion del servo
int accionEnCurso = 1;              // cantidad de ciclos ejecutando una accion
int multiplicador = 1000/interval;  // multiplica la cant de ciclos para dar tiempo a que el coche pueda girar
const int SPEED = 100;              // velocidad del coche de las 4 ruedas a la vez.

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;

  /******************************************************************
    MANEJAR GIRO de SERVO
  ******************************************************************/
    if(grados_servo<=ANGULO_MIN || grados_servo>=ANGULO_MAX){
      clockwise=!clockwise; // cambio de sentido
      grados_servo = constrain(grados_servo, ANGULO_MIN, ANGULO_MAX);
    }
    if(clockwise)
      grados_servo=grados_servo+incrementos;
    else
      grados_servo=grados_servo-incrementos;
    
    if(accionEnCurso>0){
      accionEnCurso=accionEnCurso-1;
    }else{
  /******************************************************************
    LLAMAMOS a la FUNCION DE CONDUCCION
  ******************************************************************/
       conducir();      
    }
    myservo.write(grados_servo);    
  }

}

//USA LA RED NEURONAL YA ENTRENADA
void conducir()
{
    double TestInput[] = {0, 0,0};
    double entrada1=0,entrada2=0;
    
  /******************************************************************
    OBTENER DISTANCIA DEL SENSOR
  ******************************************************************/
    double distance = double(Distance_test());
    distance= double(constrain(distance, 0.0, ditanciaMaxima));
    entrada1= ((-2.0/ditanciaMaxima)*double(distance))+1.0; //uso una funcion lineal para obtener cercania
    accionEnCurso = ((entrada1 +1) * multiplicador)+1; // si esta muy cerca del obstaculo, necestia mas tiempo de reaccion

  /******************************************************************
    OBTENER DIRECCION SEGUN ANGULO DEL SERVO
  ******************************************************************/
    entrada2 = map(grados_servo, ANGULO_MIN, ANGULO_MAX, -100, 100);
    entrada2 = double(constrain(entrada2, -100.00, 100.00));

  /******************************************************************
    LLAMAMOS A LA RED FEEDFORWARD CON LAS ENTRADAS
  ******************************************************************/
  Serial.print("Entrada1:");
  Serial.println(entrada1);
  Serial.print("Entrada2:");
  Serial.println(entrada2/100.0);

  TestInput[0] = 1.0;//BIAS UNIT
  TestInput[1] = entrada1;
  TestInput[2] = entrada2/100.0;

  InputToOutput(TestInput[0], TestInput[1], TestInput[2]); //INPUT to ANN to obtain OUTPUT

  int out1 = round(abs(Output[0]));
  int out2 = round(abs(Output[1]));
  int out3 = round(abs(Output[2]));
  int out4 = round(abs(Output[3]));
  Serial.print("Salida1:");
  Serial.println(out1);
  Serial.print("Salida2:");
  Serial.println(out2);
  Serial.println(Output[1]);
  Serial.print("Salida3:");
  Serial.println(out3);
  Serial.print("Salida4:");
  Serial.println(out4);

  /******************************************************************
    IMPULSAR MOTORES CON LA SALIDA DE LA RED
  ******************************************************************/
  int carSpeed = SPEED; //hacia adelante o atras
  if((out1+out3)==2 || (out2+out4)==2){ // si es giro, necesita doble fuerza los motores
    carSpeed = SPEED * 2;
  }
  analogWrite(ENA, carSpeed);
  analogWrite(ENB, carSpeed);
  digitalWrite(IN1, out1 * HIGH); 
  digitalWrite(IN2, out2 * HIGH); 
  digitalWrite(IN3, out3 * HIGH);
  digitalWrite(IN4, out4 * HIGH);
}

void InputToOutput(double In1, double In2, double In3)
{
  double TestInput[] = {0, 0,0};
  TestInput[0] = In1;
  TestInput[1] = In2;
  TestInput[2] = In3;

  /******************************************************************
    Calcular las activaciones en las capas ocultas
  ******************************************************************/

  for ( i = 0 ; i < HiddenNodes ; i++ ) {
    Accum = 0;//HiddenWeights[InputNodes][i] ;
    for ( j = 0 ; j < InputNodes ; j++ ) {
      Accum += TestInput[j] * HiddenWeights[j][i] ;
    }
    //Hidden[i] = 1.0 / (1.0 + exp(-Accum)) ; //Sigmoid
    Hidden[i] = tanh(Accum) ; //tanh
  }

  /******************************************************************
    Calcular activacion y error en la capa de Salida
  ******************************************************************/

  for ( i = 0 ; i < OutputNodes ; i++ ) {
    Accum = 0;//OutputWeights[HiddenNodes][i];
    for ( j = 0 ; j < HiddenNodes ; j++ ) {
        Accum += Hidden[j] * OutputWeights[j][i] ;
    }
    Output[i] = tanh(Accum) ;//tanh
  }

}


