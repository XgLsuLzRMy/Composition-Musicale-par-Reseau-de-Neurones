import keras
from keras.models import Sequential
from keras.layers import Dense, Activation,Dropout,LSTM,TimeDistributed,Bidirectional
from keras import losses
from keras import optimizers
import numpy as np
from keras import regularizers
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
	data = [[0 for y in range(3)] for x in range(dim)]
	for line in lines:
		s = re.findall(r"[-+]?\d*\.\d+|\d+\t\n\r\f\v", line)
		if i<=dim:
			data[i][0]=float(s[0])
			data[i][1]=float(s[1])
			data[i][2]=float(s[2])
		i+=1
	donnees.close()
	return data

def transformerArrayEn3D(nomFichier,dim1,dim2,dim3):
	data = transformerArrayEn2D(nomFichier,dim1*dim2)
	data = np.reshape(data,(dim1, dim2, dim3))
	X = data[np.mod(np.arange(data.shape[0]),dim2)].reshape(dim1,dim2,dim3)
	return X

def creationDonneesApprentissage(nomFichier,dim1,dim2,dim3,nbE,ePc,tS):
	X = transformerArrayEn3D(nomFichier, dim1,dim2, dim3)
	x = np.zeros(shape=(nbE, tS, dim3))
	y = np.zeros(shape=(nbE, dim3))
	print("X shape = ",X.shape) #(272, 1500, 3)
	print("x shape = ",x.shape) #(405280, 10,3)
	print("Y shape = ",y.shape) #(405280, 3)
	print(enumerate(X))
	#n va de 0 a 271
	for n, X in enumerate(X):
		for i in range(ePc):
			x[i+n*ePc][:][:] = X[i:(i+tS), :] #ePc = 1490 #i+nePc = 0 a 405279
			y[i+n*ePc][:] = X[i+tS, :] #i+tS va de 0 a 1499
	print("x shape = ",x.shape) #(405280, 10,3)
	print("Y shape = ",y.shape) #(405280, 3)
	return x,y
	
	
def creationDonneesPrediction(nomFichier,dim1,dim2,dim3):
	X = transformerArrayEn3D(nomFichier, dim1,dim2, dim3)
	x = np.zeros(shape=(nb_echantillon, taille_sequence, note_dim))
	y = np.zeros(shape=(nb_echantillon, note_dim))
	for n, X in enumerate(X):
		for i in range(echantillons_par_chanson):
			x[i+n*echantillons_par_chanson][:][:] = X[i:(i+taille_sequence), :]
	return x



taille_sequence = 10
note_dim = 3
nb_chanson = 241
nbNotes_par_chanson = 2000
echantillons_par_chanson = nbNotes_par_chanson - taille_sequence
nb_echantillon = nb_chanson*echantillons_par_chanson
batch_size = 15
epochs = 10
taux_apprentissage = 0.01
#opt = optimizers.rmsprop(taux_apprentissage)
decay_rate = taux_apprentissage / epochs
momentum = 0.8
opt = optimizers.SGD(lr=taux_apprentissage, momentum=momentum, decay=decay_rate, nesterov=False)
#opt = optimizers.Adadelta(lr=taux_apprentissage, epsilon=1e-6)
#cout = 'categorical_crossentropy'
cout = 'mean_squared_error'
nomFichierDuModele = 'modele4.h5'
imageDuModele = 'modele4.png'
nomFichierDesPoids = 'poids4.h5'



x,y = creationDonneesApprentissage("donneesNormalisees.txt",nb_chanson, nbNotes_par_chanson, note_dim,nb_echantillon,echantillons_par_chanson,taille_sequence)
print(x.shape)
nb_chanson_test  = 94
nbNotes_par_chanson_test  = 440
echantillons_par_chanson_test  = nbNotes_par_chanson_test  - taille_sequence
nb_echantillon_test  = nb_chanson_test *echantillons_par_chanson_test 
x_test,y_test = creationDonneesApprentissage("donneesTest.txt",nb_chanson_test, nbNotes_par_chanson_test, note_dim,nb_echantillon_test,echantillons_par_chanson_test,taille_sequence)

model = Sequential()
model.add(LSTM(taille_sequence, input_shape=(taille_sequence, note_dim),return_sequences=False))
#model.add(TimeDistributed(Dense(taille_sequence, activation='sigmoid')))
#model.add(Dropout(0.2))
#model.add(LSTM(taille_sequence))
#model.add(Dropout(0.2))
#model.add(Dense(note_dim, activation='sigmoid'))
model.add(Dense(y.shape[1], activation='sigmoid'))
model.add(Activation('softmax'))
plot_model(model, to_file=imageDuModele, show_shapes=True, show_layer_names=True)
model.summary()



callbacks = [
    EarlyStopping(monitor='val_loss', patience=2, verbose=0),
    ModelCheckpoint("weights.{epoch:02d}-{val_loss:.2f}.hdf5",monitor='val_loss', save_best_only=True, verbose=0),
]


model.compile(loss=cout, optimizer=opt,metrics=['accuracy'])
  
history = model.fit(x,y,verbose=1, validation_data=(x_test, y_test),batch_size=batch_size, epochs=epochs,callbacks=callbacks, shuffle=False)


##courbe de la precision sur les ensembles de donnees d'apprentissage et de validation au cours des iterations d'apprentissage.
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Precision du modele')
plt.ylabel('Precision')
plt.xlabel('Iterations')
plt.legend(['Apprentissage', 'Test'], loc='upper left')
plt.show()
## courbe de la perte/cout sur les ensembles de donnees d'apprentissage et de validation au cours des iterations d'apprentissage.
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Cout du modele')
plt.ylabel('Cout')
plt.xlabel('Iterations')
plt.legend(['Apprentissage', 'Test'], loc='upper left')
plt.show()

##obtenir les valeurs des poids par couche (utiliser le logicie HDFView)
model.save_weights(nomFichierDesPoids)

##EVALUATION
## pas utile car correspond deja a val_loss et val_acc
#loss_and_metrics = model.evaluate(x_test, y_test, batch_size=1)
#print ("Loss et metrics ",loss_and_metrics)

model.save(nomFichierDuModele)
