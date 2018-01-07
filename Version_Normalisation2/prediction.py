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

mean_tick = 84.15
std_tick = 168.49
mean_data1 = 70.42
std_data1 = 10.16
mean_data2 = 26.55 
std_data2 = 28.88
def tanhEstimators(x,moyenne,ecartType):
    return float(0.5*(np.tanh(0.01*(x-moyenne)/ecartType)+1))

def transformerArrayEn2D(nomFichier,dim):
	donnees = open(nomFichier,"r")
	lines = donnees.readlines()
	i=0
	data = [[0 for y in range(3)] for x in range(dim)]
	for line in lines:
		s = re.findall(r"[-+]?\d*\.\d+|\d+\t\n\r\f\v", line)
		if i<dim:
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

def creationDonneesPrediction(nomFichier,dim1,dim2,dim3,nbE,ePc,tS):
	X = transformerArrayEn3D(nomFichier, dim1,dim2, dim3)
	x = np.zeros(shape=(nbE, tS, dim3))
	y = np.zeros(shape=(nbE, dim3))
	for n, X in enumerate(X):
		for i in range(ePc):
			x[i+n*ePc][:][:] = X[i:(i+tS), :]
			
	return x

def normalisation(fileRead,fileWrite):
    lines = fileRead.readlines()
    tick = []
    data1 = []
    data2 = []
    for line in lines:
	    s = re.findall(r"[-+]?\d*\.\d+|\d+", line)
	    tick.append(float(s[0]))
	    data1.append(float(s[1]))
	    data2.append(float(s[2]))
    fileRead.close()
    
    max_tick = 3500
    min_tick = 0
    max_data1 = 127
    min_data1 = 0
    max_data2 = max_data1
    min_data2 = min_data1
    for i in range(0,len(tick)):
	    t = Decimal(tanhEstimators(float(tick[i]),mean_tick,std_tick))
	    if (t==0):
                t=0.0
	    if (t==1):
	        t=1.0
	    fileWrite.write(str(t)+" ")
	    d1 =  Decimal(tanhEstimators(float(data1[i]),mean_data1,std_data1))
	    if (d1==0):
                d1=0.0
	    if (d1==1):
                d1=1.0
	    fileWrite.write(str(d1)+" ")
	    d2 = Decimal(tanhEstimators(float(data2[i]),mean_data2,std_data2))
	    if (d2==0):
                d2=0.0
	    if (d2==1):
                d2=1.0
	    fileWrite.write(str(d2)+"\n")
	    if (t or d1 or d2)>1.0 or (t or d1 or d2)<0.0:
                print("Probleme de normalisation!")
                print(i)
    fileWrite.close()
    
#PREDICTION
def ecrire10NotesDansFichier(nomFinal,nomIntermediaire,note,nbIteration):	
    f = open(nomFinal,"r")
    fIntermediaire = open(nomIntermediaire,"w")
    lines = f.readlines()
    nbNotes=0
    i=1
    for line in lines:
       if i>nbIteration and nbNotes==10:
           fIntermediaire.write(str(Decimal(float(note[0][0])))+" "+str(Decimal(float(note[0][1])))+" "+str(Decimal(float(note[0][2]))) + "\n")
       if i>nbIteration and nbNotes<10:
            fIntermediaire.write(line)
            nbNotes+=1
       i+=1
    f.close()
    fIntermediaire.close()

    


model = load_model('modele.h5')
nbNotesAPredire = 9
taille_sequence = 10
note_dim = 3
nb_chanson = 1
nbNotes_par_chanson = 20
#nbNotes_par_chanson = 10
echantillons_par_chanson = nbNotes_par_chanson - taille_sequence
nb_echantillon = nb_chanson*echantillons_par_chanson
#echantillons_par_chanson =1
#nb_echantillon = nb_chanson*echantillons_par_chanson


#Normalisation du fichier d'entree et creation d'un fichier pour les 10 notes
nomTestPasNormalise = "testD.txt"
fichierPasNormalise = open(nomTestPasNormalise,"r")
nomTestNormalise = "testN.txt"
fichierNormalise = open(nomTestNormalise,"w")
nomFichier10Notes = "fichier10Notes.txt"
normalisation(fichierPasNormalise,fichierNormalise)
fichier10Notes  = open(nomFichier10Notes,"a")
fichier10Notes.write(open(nomTestNormalise).read())
fichier10Notes.close()
fichierNormalise.close()
fichierPasNormalise.close()

#creation du fichier final
nomFichierFinal = "testFinal.txt"
fichierFinal = open(nomFichierFinal,"a")
fichierFinal.write(open(nomTestNormalise).read())
fichierFinal.close()
x = creationDonneesPrediction(nomFichierFinal,nb_chanson, nbNotes_par_chanson, note_dim,nb_echantillon,echantillons_par_chanson,taille_sequence)
prediction = model.predict(x, verbose=0, batch_size=1)
with open(nomFichierFinal, "a") as fic:
    for item in prediction:
        print(item)
        fic.write(str(item[0])+" "+str(item[1])+" "+str(item[2])+"\n")
	
fichierFinal.close()
subprocess.call("python3 denormalisation.py "+nomFichierFinal+" > predictionFinale.txt", shell=True)
subprocess.call("python3 creation_midi.py predictionFinale.txt", shell=True)
os.remove(nomFichierFinal)
os.remove("predictionFinale.txt")
os.remove(nomFichier10Notes)
os.remove(nomTestNormalise)
os.remove("donneesDenormalises.txt")
subprocess.call("timidity newMusic.mid", shell=True)




