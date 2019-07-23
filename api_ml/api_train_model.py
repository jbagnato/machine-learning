import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

from utiles import *

df = pd.read_csv('time_series.csv',  parse_dates=[0], header=None,index_col=0, names=['fecha','unidades'])
df['weekday']=[x.weekday() for x in df.index]
df['month']=[x.month for x in df.index]
print(df.head())

EPOCHS=40
PASOS=7

scaler = MinMaxScaler(feature_range=(-1, 1))

reframed = transformar(df, scaler)

reordenado=reframed[ ['weekday','month','var1(t-7)','var1(t-6)','var1(t-5)','var1(t-4)','var1(t-3)','var1(t-2)','var1(t-1)','var1(t)'] ]
reordenado.dropna(inplace=True)

training_data = reordenado.drop('var1(t)', axis=1)
target_data=reordenado['var1(t)']
cant = len(df.index)
valid_data = training_data[cant-30:cant]
valid_target=target_data[cant-30:cant]

training_data = training_data[0:cant]
target_data=target_data[0:cant]
print(training_data.shape, target_data.shape, valid_data.shape, valid_target.shape)
print(training_data.head())

model = crear_modeloEmbeddings()

continuas = training_data[['var1(t-7)','var1(t-6)','var1(t-5)','var1(t-4)','var1(t-3)','var1(t-2)','var1(t-1)']]
valid_continuas = valid_data[['var1(t-7)','var1(t-6)','var1(t-5)','var1(t-4)','var1(t-3)','var1(t-2)','var1(t-1)']]

history = model.fit([training_data['weekday'],training_data['month'],continuas], target_data, epochs=EPOCHS,
                 validation_data=([valid_data['weekday'],valid_data['month'],valid_continuas],valid_target))

results = model.predict([valid_data['weekday'],valid_data['month'],valid_continuas])

print( 'Resultados escalados',results )
inverted = scaler.inverse_transform(results)
print( 'Resultados',inverted )

save_object('scaler_time_series.pkl', scaler)
model.save('red_time_series.h5')
model.save_weights("pesos.h5")

#loaded_model = load_model('red_time_series.h5')
loaded_model = crear_modeloEmbeddings()
loaded_model.load_weights("pesos.h5")

results = loaded_model.predict([valid_data['weekday'],valid_data['month'],valid_continuas])
print( 'Resultados escalados',results )
loaded_scaler = load_object('scaler_time_series.pkl')
inverted = loaded_scaler.inverse_transform(results)
print( 'Resultados',inverted )
