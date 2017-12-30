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
import re
##LES DONNEES
#fd = open("donneesNormalises.txt", 'r')
#nbLigne = 0
#for line in fd:
    #nbLigne += 1
#division = int(nbLigne/4)
#reste = nbLigne%4
#print(division*3+division+reste)
#print(nbLigne)
#donnees = np.loadtxt("donneesNormalises.txt", delimiter=" ")
#x_train = np.zeros((10, 4))
#y_train = np.zeros(4)
#print(x_train)
#print(y_train)

def transformerArrayEn2D(nomFichier):
	donnees = open(nomFichier,"r")
	lines = donnees.readlines()
	i=0
	data = [[0 for x in range(4)] for y in range(1000)]
	for line in lines:
		s = re.findall(r"[-+]?\d*\.\d+|\d+\t\n\r\f\v", line)
		data[i][0]=float(s[0])
		data[i][1]=float(s[1])
		data[i][2]=float(s[2])
		data[i][3]=float(s[3])
		i+=1
	donnees.close()
	return data

def transformerArrayEn3D(nomFichier,dim1,dim2,dim3):
	data = transformerArrayEn2D(nomFichier)
	data = np.reshape(data,(dim1, dim2, dim3))
	X = data[np.mod(np.arange(data.shape[0]),number_of_notes_per_song)!=0].reshape(dim1,dim2-1,dim3)
	return X

#donnees = open("data.txt","r")
#lines = donnees.readlines()
#i=0
#data = [[0 for x in range(4)] for y in range(1000)]
#for line in lines:
	#s = re.findall(r"[-+]?\d*\.\d+|\d+\t\n\r\f\v", line)
	#data[i][0]=float(s[0])
	#data[i][1]=float(s[1])
	#data[i][2]=float(s[2])
	#data[i][3]=float(s[3])
	#i+=1
#donnees.close()

data = transformerArrayEn2D("data.txt")

#assuming all 4 columns correspond to 1 song
data_dim = 4
#so one song would be 10x4 2D array 
number_of_notes_per_song = 10
nsongs_train = 100
#tunable parameter
batch_size = 32
epochs = 5
nomFichierDuModele = 'modele.h5'
nomFichierDesPoids = 'poids.h5'

#x_train = transformerArrayEn3D(data,nsongs_train, number_of_notes_per_song, data_dim)
x_train = np.reshape(data,(nsongs_train, number_of_notes_per_song, data_dim))
#this is a supervised learning problem, but your dataset has no labels..
#we can use last note in each song as a label when training LSTM 
X = x_train[np.mod(np.arange(x_train.shape[0]),number_of_notes_per_song)!=0].reshape(nsongs_train,number_of_notes_per_song-1,data_dim)
y = x_train[::number_of_notes_per_song].reshape(nsongs_train,data_dim) 

model = Sequential()
model.add(LSTM(32, input_shape=(number_of_notes_per_song-1, data_dim),return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(64))
model.add(Dropout(0.2))
model.add(Dense(data_dim, activation='softmax'))

plot_model(model, to_file='modele.png', show_shapes=True, show_layer_names=True)
model.summary()

model.compile(loss='categorical_crossentropy', optimizer='adam')

history = model.fit(X,y,batch_size=batch_size, epochs=epochs)





#courbe de la precision sur les ensembles de donnees d'apprentissage et de validation au cours des iterations d'apprentissage.

# courbe de la perte/cout sur les ensembles de donnees d'apprentissage et de validation au cours des iterations d'apprentissage.
plt.plot(history.history['loss'])
#plt.plot(history.history['val_loss'])
plt.title('Cout du modele')
plt.ylabel('Cout')
plt.xlabel('Iterations')
plt.legend(['Apprentissage', 'Test'], loc='upper left')
plt.show()

#obtenir les valeurs des poids par couche (utiliser le logicie HDFView)
model.save_weights(nomFichierDesPoids)

#EVALUATION
loss_and_metrics = model.evaluate(X, y, batch_size=1)
print ("Loss et metrics ",loss_and_metrics)

#PREDICTION
test = transformerArrayEn3D("test.txt",100,10,4)
previsions = model.predict(test)
np.savetxt('prediction.txt', previsions)

#sauvegarder le modele
model.save(nomFichierDuModele)
