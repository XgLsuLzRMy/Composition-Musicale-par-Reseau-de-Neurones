import keras
from keras.models import load_model
import re
import numpy as np

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
	



taille_sequence = 10

nb_chanson_test  = 94
nbNotes_par_chanson_test  = 440
note_dim = 3
echantillons_par_chanson_test  = nbNotes_par_chanson_test  - taille_sequence
nb_echantillon_test  = nb_chanson_test *echantillons_par_chanson_test


x_test,y_test = creationDonneesApprentissage("donneesTest.txt",nb_chanson_test, nbNotes_par_chanson_test, note_dim,nb_echantillon_test,echantillons_par_chanson_test,taille_sequence)

model = load_model('modele4.h5')
model.summary()

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=1)
print ("Loss et metrics ",loss_and_metrics)