import keras
from keras.models import Sequential
from keras.layers import Dense, Activation,Dropout,LSTM
from keras import losses
from keras import optimizers
import numpy as np
from keras.utils import plot_model
from keras.models import load_model
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping
#LES DONNEES
fd = open("donneesNormalises.txt", 'r')
nbLigne = 0
for line in fd:
    nbLigne += 1
division = int(nbLigne/4)
reste = nbLigne%4
print(division*3+division+reste)
print(nbLigne)
donnees = np.loadtxt("donneesNormalises.txt", delimiter=" ")
x_train = np.zeros((10, 4))
y_train = np.zeros(4)
print(x_train)
print(y_train)
#CREATION DU MODELE
model = Sequential()
model.add(Dense(4, activation='relu',input_shape = (10,4),name='couche1'))
model.add(Dense(20, activation='relu',name='couche2'))
model.add(Dense(20, activation='relu',name='couche3'))
model.add(Dense(4, activation='relu',name='couche4'))
model.add(Dense(4, activation='relu',name='couche5'))
plot_model(model, to_file='modele.png', show_shapes=True, show_layer_names=True)
model.summary()


learning_rate = 0.01
sgd = optimizers.SGD(learning_rate)
cout = 'mean_squared_error'
model.compile(loss=cout,optimizer=sgd,metrics=['accuracy'])

model.fit(x_train, y_train,epochs=1,batch_size=1, verbose=1,shuffle=True )
