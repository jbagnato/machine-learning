# Object tracking con Yolo v8 y algoritmo ByteTrack

## Clona el repositorio

Primero clona o descarga este repositorio que contiene los archivos necesarios.

OPCIóN 1: Puedes clonar el repo completo con:

```sh
git clone https://github.com/jbagnato/machine-learning.git
cd machine-learning
```

OPCIóN 2: si sólo vas a utilizar el proyecto `yolo_tracking` puedes hacer:

```sh
git clone -n --depth=1 --filter=tree:0 https://github.com/jbagnato/machine-learning.git
cd machine-learning
git sparse-checkout set --no-cone yolo_tracking
git checkout
```

y luego te mueves al directorio de yolo_tracking

## Instalación del ambiente de desarrollo

Instala un environment de python 3.9. Si tienes Anaconda instalado puedes hacerlo ejecutando:

```sh
    conda create -n tracking python=3.9 numpy
```

Y luego activa el ambiente con

```sh
    conda activate tracking
```


> NOTA: En Windows, será necesario que instales las librerias de C++. Para ello deberás descargar e instalarlas mediante este enlace:
Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/

> NOTA: en Mac puede necesitar instalar una libreria adicional mediante `conda install nomkl`

luego instalamos los requerimientos para el proyecto:

```sh
    pip install -r requirements.txt
```

## Uso del Script de tracking

Al ejecutar por primera vez, se descargará automaticamente el modelo de Yolo yolov8n.pt de 6MB

```sh
python detectar.py -v skateboard_01.mp4
```

## Si vas a usar la version Jupyter Notebook

Si vas a ejecutar la versión Notebook, primero deberás instalar:

```sh
conda install -n tracking ipykernel --update-deps --force-reinstall
```
