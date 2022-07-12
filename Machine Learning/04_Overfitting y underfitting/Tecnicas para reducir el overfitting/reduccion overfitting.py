#
# Importación de librerías
#

import numpy as np
import matplotlib.pyplot as plt

# Pre-procesamiento de datos
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Modelos en Keras (incluyendo Droput y Early Stopping)
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping

#
# Función para graficar resultados
#
def graficar_resultados(historia):
	plt.subplot(1,2,1)
	plt.plot(historia.history['loss'])
	plt.plot(historia.history['val_loss'])
	plt.ylabel('Pérdida')
	plt.xlabel('Iteración')
	plt.legend(['Entrenamiento','Validación'])

	plt.subplot(1,2,2)
	plt.plot(historia.history['acc'])
	plt.plot(historia.history['val_acc'])
	plt.ylabel('Precisión')
	plt.xlabel('Iteración')
	plt.legend(['Entrenamiento','Validación'])

	ax = plt.gca()
	ax.yaxis.set_label_position("right")
	ax.yaxis.tick_right()

	plt.show()

#
# Lectura y pre-procesamiento de datos
# 
dataset = np.loadtxt("dataset.csv", delimiter=",")
X = dataset[:, 0:8]
Y = dataset[:, 8]

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

#
# Creación, entrenamiento y validación de los modelos
#

np.random.seed(100)
# 1. Modelo de base: 2 capas ocultas con 1000 y 250 neuronas
model = Sequential()
model.add(Dense(1000, input_dim=8, activation='relu'))
model.add(Dense(250, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
historia = model.fit(x_train, y_train, batch_size=64, epochs=150, validation_data=(x_test,y_test), verbose=1)

graficar_resultados(historia)

# 2. Modelo simplificado: 1 capa oculta con 100 neuronas
model = Sequential()
model.add(Dense(100, input_dim=8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
historia = model.fit(x_train, y_train, batch_size=64, epochs=150, validation_data=(x_test,y_test), verbose=1)

graficar_resultados(historia)

# 3. Modelo base con dropout
model = Sequential()
model.add(Dense(1000, input_dim=8, activation='relu'))
model.add(Dropout(0.9))
model.add(Dense(250, activation='relu'))
model.add(Dropout(0.8))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
historia = model.fit(x_train, y_train, batch_size=64, epochs=150, validation_data=(x_test,y_test), verbose=1)

graficar_resultados(historia)

# 4. Modelo con droput y early stopping
model = Sequential()
model.add(Dense(1000, input_dim=8, activation='relu'))
model.add(Dropout(0.9))
model.add(Dense(250, activation='relu'))
model.add(Dropout(0.8))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

early_stop = EarlyStopping(monitor='val_loss', patience=4, restore_best_weights=True)
historia = model.fit(x_train, y_train, batch_size=64, epochs=150, validation_data=(x_test,y_test), verbose=1, callbacks=[early_stop])

graficar_resultados(historia)


