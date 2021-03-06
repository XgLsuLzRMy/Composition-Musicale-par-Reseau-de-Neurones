import keras
from keras.models import Sequential
from keras.layers import Dense, Activation,Dropout,LSTM,TimeDistributed
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
	X = data[np.mod(np.arange(data.shape[0]),dim2)].reshape(dim1,dim2,dim3)
	return X

def creationDonneesApprentissage(nomFichier,dim1,dim2,dim3,nbE,ePc,tS,notedim):
	X = transformerArrayEn3D(nomFichier, dim1,dim2, dim3)
	x = np.zeros(shape=(nbE, tS, notedim))
	y = np.zeros(shape=(nbE, notedim))
	for n, X in enumerate(X):
		for i in range(ePc):
			x[i+n*ePc][:][:] = X[i:(i+tS), :]
			y[i+n*ePc][:][:] = X[i+tS, :] # note that you want to predict
	return x,y
	
	
def creationDonneesPrediction(nomFichier,dim1,dim2,dim3):
	X = transformerArrayEn3D(nomFichier, dim1,dim2, dim3)
	x = np.zeros(shape=(nb_echantillon, taille_sequence, note_dim))
	y = np.zeros(shape=(nb_echantillon, note_dim))
	for n, X in enumerate(X):
		for i in range(echantillons_par_chanson):
			x[i+n*echantillons_par_chanson][:][:] = X[i:(i+taille_sequence), :]
	return x



taille_sequence = 20
note_dim = 4
nb_chanson = 244
nbNotes_par_chanson = 2000
echantillons_par_chanson = nbNotes_par_chanson - taille_sequence
nb_echantillon = nb_chanson*echantillons_par_chanson
data_dim = 4 
batch_size = 50
epochs = 10
taux_apprentissage = 0.001
#opt = optimizers.rmsprop(taux_apprentissage)
opt = optimizers.rmsprop(taux_apprentissage)
cout = 'categorical_crossentropy'
#cout = 'mean_squared_error'
nomFichierDuModele = 'modele.h5'
imageDuModele = 'modele.png'
nomFichierDesPoids = 'poids.h5'



x,y = creationDonneesApprentissage("donneesNormalisees.txt",nb_chanson, nbNotes_par_chanson, data_dim,nb_echantillon,echantillons_par_chanson,taille_sequence,note_dim)

taille_sequence_test = 20
nb_chanson_test  = 88
nbNotes_par_chanson_test  = 400
echantillons_par_chanson_test  = nbNotes_par_chanson_test  - taille_sequence
nb_echantillon_test  = nb_chanson_test *echantillons_par_chanson_test 
x_test,y_test = creationDonneesApprentissage("donneesTest.txt",nb_chanson_test, nbNotes_par_chanson_test, data_dim,nb_echantillon_test,echantillons_par_chanson_test,taille_sequence,note_dim)

model = Sequential()
model.add(LSTM(32, input_shape=(taille_sequence, note_dim),return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(data_dim))
model.add(Dense(data_dim, activation='relu',activity_regularizer=regularizers.l2(0.1)))
model.add(Dense(data_dim, activation='sigmoid',activity_regularizer=regularizers.l2(0.1)))
model.add(TimeDistributed(Dense(1)))
plot_model(model, to_file=imageDuModele, show_shapes=True, show_layer_names=True)
model.summary()


model.compile(loss=cout, optimizer=opt,metrics=['accuracy'])
  
history = model.fit(x,y,verbose=1, validation_data=(x_test, y_test),batch_size=batch_size, epochs=epochs, shuffle=True)


#courbe de la precision sur les ensembles de donnees d'apprentissage et de validation au cours des iterations d'apprentissage.
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Precision du modele')
plt.ylabel('Precision')
plt.xlabel('Iterations')
plt.legend(['Apprentissage', 'Test'], loc='upper left')
plt.show()
# courbe de la perte/cout sur les ensembles de donnees d'apprentissage et de validation au cours des iterations d'apprentissage.
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Cout du modele')
plt.ylabel('Cout')
plt.xlabel('Iterations')
plt.legend(['Apprentissage', 'Test'], loc='upper left')
plt.show()

#obtenir les valeurs des poids par couche (utiliser le logicie HDFView)
model.save_weights(nomFichierDesPoids)

#EVALUATION
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=1)
print ("Loss et metrics ",loss_and_metrics)
model.save(nomFichierDuModele)






# Chargement du modele stocke dans le fichier pour le reutiliser
# model = load_model(nomFichierDuModele)

##PREDICTION
#note_dim = 4
#taille_sequence = 10
#nb_chanson = 1
#nbNotes_par_chanson = 10
#echantillons_par_chanson = 1
#nb_echantillon = nb_chanson*echantillons_par_chanson

#nomTest = "test.txt"
#open("fin.txt","a").write(open(nomTest).read())
#prediction='prediction.txt'
#predictionFin ="predictionNormalisee.txt"



#x = creationDonneesPrediction(nomTest, nb_chanson,taille_sequence,note_dim)
#previsions = model.predict(x, verbose=0)[0]
#np.savetxt(prediction, previsions[None], fmt="%f",delimiter=' ')
#open(predictionFin,"w").write(open(nomTest).read() + open(prediction).read())

#subprocess.call("python3 denormalisation.py "+predictionFin+" > predictionBB.txt", shell=True)
#subprocess.call("python3 creation_midi.py predictionBB.txt", shell=True)
#subprocess.call("timidity newMusic.mid", shell=True)

