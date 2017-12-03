from keras.models import Sequential
from keras.layers import Activation, Dense

# On instancie le modele
model = sequential()
# ajoute la premiere couche
model.add(Dense(n1, input_shape(300,), activation='relu'))
# on ajoute une deuxieme couche
model.add(Dense(n2, activation='sigmoid'))
# la derniere couche
model.add(Dense(n3, activation='tanh'))