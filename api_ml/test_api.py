import json
import requests
import pandas as pd
import pickle
from utiles import *

"""Setting the headers to send and accept json responses
"""
header = {'Content-Type': 'application/json', \
                  'Accept': 'application/json'}

# creamos un dataset de pruebas
df = pd.DataFrame({"unidades": [289,288,260,240,290,255,270,300], 
					"weekday": [5,0,1,2,3,4,5,0], 
					"month":   [4,4,4,4,4,4,4,4]})

loaded_scaler = load_object('scaler_time_series.pkl')

reframed = transformar(df, loaded_scaler)

reordenado=reframed[ ['weekday','month','var1(t-7)','var1(t-6)','var1(t-5)','var1(t-4)','var1(t-3)','var1(t-2)','var1(t-1)'] ]
reordenado.dropna(inplace=True)
#print(reordenado)

"""Converting Pandas Dataframe to json
"""
data = reordenado.to_json(orient='records')

print('JSON para enviar en POST', data)

"""POST <url>/predict
"""
resp = requests.post("http://localhost:8000/predict", \
                    data = json.dumps(data),\
                    headers= header)
                    
print('status',resp.status_code)


print('Respuesta de Servidor')
print(resp.json())

