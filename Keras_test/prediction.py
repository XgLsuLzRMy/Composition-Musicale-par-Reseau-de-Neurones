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
from decimal import Decimal

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

def normalisation(nom):
    fichierTest = open("test.txt", "w")
    donnees = open(nom,"r")
    lines = donnees.readlines()
    event = []
    tick = []
    data1 = []
    data2 = []
    for line in lines:
	    s = re.findall(r"[-+]?\d*\.\d+|\d+", line)
	    event.append(float(s[0]))
	    tick.append(float(s[1]))
	    data1.append(float(s[2]))
	    data2.append(float(s[3]))
    donnees.close()
    
    max_event = 1
    min_event = 0
    max_tick = 155520
    min_tick = 0
    max_data1 = 127
    min_data1 = 0
    max_data2 = max_data1
    min_data2 = min_data1
    for i in range(0,len(event)):
	    e = float(event[i])
	    fichierTest.write(str(e)+" ")
	    t = Decimal((float(tick[i])-min_tick)/(max_tick- min_tick))
	    if (t==0):
                t=0.0
	    if (t==1):
	        t=1.0
	    fichierTest.write(str(t)+" ")
	    d1 = Decimal((float(data1[i])-min_data1)/(max_data1- min_data1))
	    if (d1==0):
                d1=0.0
	    if (d1==1):
                d1=1.0
	    fichierTest.write(str(d1)+" ")
	    d2 = Decimal((float(data2[i])-min_data2)/(max_data2 - min_data2))
	    if (d2==0):
                d2=0.0
	    if (d2==1):
                d2=1.0
	    fichierTest.write(str(d2)+"\n")
	    if (e or t or d1 or d2)>1.0 or (e or t or d1 or d2)<0.0:
                print("Probleme de normalisation!")
                print(i)
    fichierTest.close()
    
#PREDICTION
def ecrire10NotesDansFichier(nomFinal,nomIntermediaire,note,nbIteration):	
    f = open(nomFinal,"r")
    fIntermediaire = open(nomIntermediaire,"w")
    lines = f.readlines()
    nbNotes=0
    i=1
    for line in lines:
       if i>nbIteration and nbNotes==10:
           fIntermediaire.write(str(Decimal(float(note[0][0])))+" "+str(Decimal(float(note[0][1])))+" "+str(Decimal(float(note[0][2])))+" "+str(Decimal(float(note[0][3]))) + "\n")
       if i>nbIteration and nbNotes<10:
            fIntermediaire.write(line)
            nbNotes+=1
       i+=1
    f.close()
    fIntermediaire.close()

    


model = load_model('modele.h5')
note_dim = 4
taille_sequence = 20
nb_chanson = 1
nbNotes_par_chanson = 20
echantillons_par_chanson = 1
nb_echantillon = nb_chanson*echantillons_par_chanson

nbNotesAPredire = 1


nomTest = "testD.txt"
nomFinal= "testPrediction.txt"
nomIntermediaire = "testIntermediaire.txt"
fichierTest1 = open(nomTest,"r")
normalisation(nomTest)
fichierFinal = open(nomFinal,"w")
fichierIntermediaire = open(nomIntermediaire,"w")
fichierIntermediaire.write(open("test.txt").read())
fichierFinal.write(open("test.txt").read())

fichierFinal.close()
fichierIntermediaire.close()


for iteration in range(1,nbNotesAPredire+1):
    x = creationDonneesPrediction(nomIntermediaire, nb_chanson,taille_sequence,note_dim)
    previsions = model.predict(x, verbose=0)
    fichierFinal = open(nomFinal,"a")
    print(previsions)
    fichierFinal.write(str(Decimal(float(previsions[0][0])))+" "+str(Decimal(float(previsions[0][1])))+" "+str(Decimal(float(previsions[0][2])))+" "+str(Decimal(float(previsions[0][3]))) + "\n")
    fichierFinal.close()
    ecrire10NotesDansFichier(nomFinal,nomIntermediaire,previsions,iteration+9)


fichierTest1.close()
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


