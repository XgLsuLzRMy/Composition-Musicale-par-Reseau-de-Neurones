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

def creationDonneesPrediction(nomFichier,dim1,dim2,dim3):
	X = transformerArrayEn3D(nomFichier, dim1,dim2, dim3)
	x = np.zeros(shape=(nb_echantillon, taille_sequence, note_dim))
	y = np.zeros(shape=(nb_echantillon, note_dim))
	for n, X in enumerate(X):
		for i in range(echantillons_par_chanson):
			x[i+n*echantillons_par_chanson][:][:] = X[i:(i+taille_sequence), :]
	return x



#PREDICTION
model = load_model('modele.h5')
note_dim = 4
taille_sequence = 10
nb_chanson = 1
nbNotes_par_chanson = 10
echantillons_par_chanson = 1
nb_echantillon = nb_chanson*echantillons_par_chanson

nomTest = "test.txt"
open("fin.txt","a").write(open(nomTest).read())
prediction='prediction.txt'
predictionFin ="predictionNormalisee.txt"




x = creationDonneesPrediction(nomTest, nb_chanson,taille_sequence,note_dim)
previsions = model.predict(x, verbose=0)[0]
np.savetxt(prediction, previsions[None], fmt="%f",delimiter=' ')
open(predictionFin,"w").write(open(nomTest).read() + open(prediction).read())

subprocess.call("python3 denormalisation.py "+predictionFin+" > predictionBB.txt", shell=True)
subprocess.call("python3 creation_midi.py predictionBB.txt", shell=True)
subprocess.call("timidity newMusic.mid", shell=True)


