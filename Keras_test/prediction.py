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
		if i<dim:
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

def creationDonneesPrediction(nomFichier,dim1,dim2,dim3):
	X = transformerArrayEn3D(nomFichier, dim1,dim2, dim3)
	x = np.zeros(shape=(nb_echantillon, taille_sequence, note_dim))
	y = np.zeros(shape=(nb_echantillon, note_dim))
	for n, X in enumerate(X):
		for i in range(echantillons_par_chanson):
			x[i+n*echantillons_par_chanson][:][:] = X[i:(i+taille_sequence), :]
	return x



#PREDICTION
def ecrire10NotesDansFichier(nomFinal,nomIntermediaire,note,nbIteration):	
    f = open(nomFinal,"r")
    fIntermediaire = open(nomIntermediaire,"w")
    lines = f.readlines()
    nbNotes=0
    i=1
    for line in lines:
       if i>nbIteration and nbNotes==10:
           fIntermediaire.write(str(note[0][0])+" "+str(note[0][1])+" "+str(note[0][2])+" "+str(note[0][3]) + "\n")
       if i>nbIteration and nbNotes<10:
            fIntermediaire.write(line)
            nbNotes+=1
       i+=1
    f.close()
    fIntermediaire.close()
    #fIntermediaire = open(nomIntermediaire,"r")
    #lines = fIntermediaire.readlines()
    #for line in lines:
       #print(line)
    #fIntermediaire.close()
    


model = load_model('modele.h5')
note_dim = 4
taille_sequence = 10
nb_chanson = 1
nbNotes_par_chanson = 20
echantillons_par_chanson = 1
nb_echantillon = nb_chanson*echantillons_par_chanson

nbNotesAPredire = 3


nomTest = "test.txt"
nomFinal= "testPrediction.txt"
nomIntermediaire = "testIntermediaire.txt"
fichierTest = open(nomTest,"r")
fichierFinal = open(nomFinal,"w")
fichierIntermediaire = open(nomIntermediaire,"w")
fichierIntermediaire.write(open(nomTest).read())
fichierFinal.write(open(nomTest).read())

fichierFinal.close()
fichierIntermediaire.close()


for iteration in range(1,nbNotesAPredire+1):
    x = creationDonneesPrediction(nomIntermediaire, nb_chanson,taille_sequence,note_dim)
    previsions = model.predict(x, verbose=0)
    fichierFinal = open(nomFinal,"a")
    fichierFinal.write(str(previsions[0][0])+" "+str(previsions[0][1])+" "+str(previsions[0][2])+" "+str(previsions[0][3]) + "\n")
    fichierFinal.close()
    ecrire10NotesDansFichier(nomFinal,nomIntermediaire,previsions,iteration)


fichierTest.close()
fichierFinal.close()
fichierIntermediaire.close()

subprocess.call("python3 denormalisation.py "+nomFinal+" > predictionFinale.txt", shell=True)
subprocess.call("python3 creation_midi.py predictionFinale.txt", shell=True)
subprocess.call("timidity newMusic.mid", shell=True)


#open(nomFinal,"a").write(open(nomTest).read())
#prediction='prediction.txt'
#predictionFin ="predictionNormalisee.txt"

#x = creationDonneesPrediction(nomFinal, nb_chanson,taille_sequence,note_dim)
#previsions = model.predict(x, verbose=0)[0]
#np.savetxt(prediction, previsions[None], fmt="%f",delimiter=' ')
#open(predictionFin,"w").write(open(nomTest).read() + open(prediction).read())

#subprocess.call("python3 denormalisation.py "+predictionFin+" > predictionBB.txt", shell=True)
#subprocess.call("python3 creation_midi.py predictionBB.txt", shell=True)
#subprocess.call("timidity newMusic.mid", shell=True)


