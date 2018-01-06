import keras
from keras.models import Sequential
from keras.layers import Dense, Activation,Dropout,LSTM,TimeDistributed
from keras import losses
from keras import optimizers
import numpy as np
from keras.utils import plot_model
from keras.models import load_model
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping,ModelCheckpoint
import sys
import re
import subprocess
import os

def transformerArrayEn2D(nomFichier,dim):
	donnees = open(nomFichier,"r")
	lines = donnees.readlines()
	i=0
	data = [[0 for y in range(4)] for x in range(dim)]
	for line in lines:
		s = re.findall(r"[-+]?\d*\.\d+|\d+\t\n\r\f\v", line)
		if i<=dim:
			data[i][0]=float(s[0])
			data[i][1]=float(s[1])
			data[i][2]=float(s[2])
			data[i][3]=float(s[3])
		i+=1
	donnees.close()
	return data

def transformerArrayEn3D(nomFichier,dim1,dim2,dim3):
	data = transformerArrayEn2D(nomFichier,dim1*dim2)
	data = np.reshape(data,(dim1, dim2, dim3))
	print(data.shape)
	print(np.arange(data.shape[0]))
	print(np.mod(np.arange(data.shape[0]),dim2)!=0)
	X = data[np.mod(np.arange(data.shape[0]),dim2)].reshape(dim1,dim2,dim3)
	print(np.array(X).shape)
	return X




#assuming all 4 columns correspond to 1 song
data_dim = 4
#so one song would be 10x4 2D array 
number_of_notes_per_song = 1000
nsongs_train = 2
#tunable parameter
batch_size = 12
epochs = 2
learning_rate = 0.001
opt = optimizers.rmsprop(learning_rate)
cout = 'categorical_crossentropy'
nomFichierDuModele = 'modele.h5'
nomFichierDesPoids = 'poids.h5'

data = transformerArrayEn2D("data.txt",number_of_notes_per_song*nsongs_train)
x_train = np.reshape(data,(nsongs_train, number_of_notes_per_song, data_dim))
X = transformerArrayEn3D("data.txt",nsongs_train, number_of_notes_per_song, data_dim)
#y = x_train[::number_of_notes_per_song].reshape(nsongs_train,data_dim) 


batch_size = 32
window_length = 10
note_dim = 4
n_songs = 2
notes_per_song = 1000
# Suppose that variable ´songs´ is an array with shape: (n_songs, notes_per_song, note_dim). 
samples_per_song = notes_per_song - window_length
print("X shape ", X.shape)
print("Samples per song ", samples_per_song)
n_samples = n_songs*samples_per_song
print("n_samples ", n_samples)
x = np.zeros(shape=(n_samples, window_length, note_dim))
y = np.zeros(shape=(n_samples, note_dim))
for n, X in enumerate(X):
    for i in range(samples_per_song):
        x[i+n*samples_per_song][:][:] = X[i:(i+window_length), :]
        y[i+n*samples_per_song][:][:] = X[i+window_length, :] # note that you want to predict
# ...

print("x shape ", x.shape)


model = Sequential()
model.add(LSTM(32, input_shape=(10, note_dim),return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(64))
model.add(Dense(data_dim, activation='linear'))
model.add(Dense(data_dim, activation='sigmoid'))
plot_model(model, to_file='modele.png', show_shapes=True, show_layer_names=True)
model.summary()


model.compile(loss=cout, optimizer=opt,metrics=['accuracy'])
  
history = model.fit(x,y,batch_size=batch_size, epochs=epochs)




#courbe de la precision sur les ensembles de donnees d'apprentissage et de validation au cours des iterations d'apprentissage.
#plt.plot(history.history['acc'])
#plt.title('Precision du modele')
#plt.ylabel('Precision')
#plt.xlabel('Iterations')
#plt.legend(['Apprentissage', 'Test'], loc='upper left')
#plt.show()
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
loss_and_metrics = model.evaluate(x, y, batch_size=1)
print ("Loss et metrics ",loss_and_metrics)
model.save(nomFichierDuModele)






# Chargement du modele stocke dans le fichier pour le reutiliser
# model = load_model(nomFichierDuModele)



#PREDICTION
nomTest = "test.txt"
open("fin.txt","a").write(open(nomTest).read())
prediction='prediction.txt'
predictionFin ="predictionNormalisee.txt"


window_length = 10
note_dim = 4
n_songs = 1
notes_per_song = 10
# Suppose that variable ´songs´ is an array with shape: (n_songs, notes_per_song, note_dim). 
samples_per_song = 1
n_samples = n_songs*samples_per_song
test = transformerArrayEn3D(nomTest,1,10,data_dim)
print("Test shape ", test.shape)
x = np.zeros(shape=(n_samples, window_length, note_dim))
y = np.zeros(shape=(n_samples, note_dim))
for n, test in enumerate(test):
    for i in range(samples_per_song):
        x[i+n*samples_per_song][:][:] = test[i:(i+window_length), :]

print("New Test shape ", x.shape)


previsions = model.predict(x, verbose=0)[0]
np.savetxt(prediction, previsions[None], fmt="%f",delimiter=' ')
open(predictionFin,"w").write(open(nomTest).read() + open(prediction).read())




subprocess.call("python3 denormalisation.py "+predictionFin+" > predictionBB.txt", shell=True)
subprocess.call("python3 creation_midi.py predictionBB.txt", shell=True)
subprocess.call("timidity newMusic.mid", shell=True)


#sauvegarder le modele
model.save(nomFichierDuModele)
