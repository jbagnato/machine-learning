import pickle
import pandas as pd

EPOCHS=40
PASOS=7

def save_object(filename, object):
	with open(''+filename, 'wb') as file:
		pickle.dump(object, file)

def load_object(filename):
	with open(''+filename ,'rb') as f:
		loaded = pickle.load(f)
	return loaded

# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
    n_vars = 1 if type(data) is list else data.shape[1]
    df = pd.DataFrame(data)
    cols, names = list(), list()
    # input sequence (t-n, ... t-1)
    for i in range(n_in, 0, -1):
        cols.append(df.shift(i))
        names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
    # forecast sequence (t, t+1, ... t+n)
    for i in range(0, n_out):
        cols.append(df.shift(-i))
        if i == 0:
            names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
        else:
            names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
    # put it all together
    agg = pd.concat(cols, axis=1)
    agg.columns = names
    # drop rows with NaN values
    if dropnan:
        agg.dropna(inplace=True)
    return agg

def crear_modeloEmbeddings():
	from keras.models import Sequential
	from keras.layers import Activation, Input, Embedding, Dense, Flatten, Dropout, concatenate, LSTM
	from keras.layers import BatchNormalization, SpatialDropout1D
	from keras.callbacks import Callback
	from keras.models import Model
	from keras.optimizers import Adam
	from keras.models import load_model

	emb_dias = 2 #tamanio profundidad de embeddings
	emb_meses = 4

	in_dias = Input(shape=[1,], name = 'dias')
	emb_dias = Embedding(7+1, emb_dias)(in_dias)
	in_meses = Input(shape=[1,], name = 'meses')
	emb_meses = Embedding(12+1, emb_meses)(in_meses)
	in_cli = Input(shape=[PASOS,], name = 'cli')
	fe = concatenate([(emb_dias), (emb_meses)])
	x = Flatten()(fe)
	x = Dense(PASOS,activation='tanh')(x)
	outp = Dense(1,activation='tanh')(x)
	model = Model(inputs=[in_dias,in_meses,in_cli], outputs=outp)
	model.compile(loss='mean_absolute_error', 
				optimizer='adam',
				metrics=['MSE'])
	return model

def transformar(df, scaler):
	# cargar valpres
	values = df['unidades'].values
	# pasar a tipo float
	values = values.astype('float32')
	# normalizar features
	values = values.reshape(-1, 1) # esto lo hacemos porque tenemos 1 sola dimension
	scaled = scaler.fit_transform(values)

	reframed = series_to_supervised(scaled, PASOS, 1)
	reframed.reset_index(inplace=True, drop=True)

	contador=0
	reframed['weekday']=df['weekday']
	reframed['month']=df['month']

	for i in range(reframed.index[0], reframed.index[-1]):
		reframed['weekday'].loc[contador]=df['weekday'][i+8]
		reframed['month'].loc[contador]=df['month'][i+8]
		contador=contador+1
	#print(reframed.head())
	return reframed
