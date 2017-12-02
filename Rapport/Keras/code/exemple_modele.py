from keras.models import Sequential
from keras.layers import Activation, Dense

# On instancie le modèle
model = sequential()
# ajoute la première couche
model.add(Dense(n1, input_shape(300,), activation='relu'))
# on ajoute une deuxième couche
model.add(Dense(n2, activation='sigmoid'))
# la dernière couche
model.add(Dense(n3, activation='tanh'))