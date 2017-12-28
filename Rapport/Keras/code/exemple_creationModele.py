import keras
from keras.models import Sequential
from keras.layers import Dense, Activation,Dropout
from keras import losses
from keras import optimizers
import numpy as np
from keras.utils import plot_model
from keras.models import load_model
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping
#LES DONNEES
#si  on a un fichier particulier 
x_train = np.loadtxt("x_train.csv", delimiter=",")
y_train = np.loadtxt("y_train.csv", delimiter=",")
x_test = np.loadtxt("x_test.csv", delimiter=",")
y_test = np.loadtxt("y_test.csv", delimiter=",")
#Y = dataset[:,3]
#np.savetxt("X.csv",X, delimiter=",")
#np.savetxt("Y.csv",Y, delimiter=",")
#seed = 7
#np.random.seed(seed)
#tableau de random de taille 10 x 1
#x_train = np.random.random((9, 1))
#y_train = keras.utils.to_categorical(np.random.randint(9, size=(9, 1)), num_classes=9)
#tableau de random de taille 20 x 1
#x_test = np.random.random((20, 1))
#y_test = keras.utils.to_categorical(np.random.randint(9, size=(20, 1)), num_classes=9)
#np.savetxt('x_train.txt', x_train)
#np.savetxt('y_train.txt', y_train)
#np.savetxt('x_test.txt', x_test)
#np.savetxt('y_test.txt', y_test)
nomFichierDuModele = 'modele.h5'
nomFichierDesPoids = 'poids.h5'

#CREATION DU MODELE

#creation d'un reseau de neurones Perceptron multi-couches vide
model = Sequential()
#ajout d'une couche completement connectee avec 32 neurones et cette couche attend 100 valeurs en entree avec la fonction d'activation relu
#input_dim = nombre de colonnes dans nos donnees
model.add(Dense(20, activation='relu', input_dim=3,name='couche1'))
#apres la premiere couche il n'est pas necessaire de specifier imput_dim
model.add(Dense(20, activation='relu',name='couche2'))
model.add(Dense(20, activation='relu',name='couche3'))
model.add(Dense(10, activation='relu',name='couche4'))
model.add(Dense(1, activation='relu', name='couche5'))
#visualiser  le modele du reseau
plot_model(model, to_file='modele.png', show_shapes=True, show_layer_names=True)
#visualisation sous forme de tableau de l'architecture du reseau
model.summary()


#METHODE DOPTIMISATION ET COMPILATION DU MODELE

#le taux d'apprentissage
learning_rate = 0.01
#definition de la methode d'optimisation: ici on prend descente de gradient stochastique SGD
sgd = optimizers.SGD(learning_rate)
#definition du cout: erreur quadratique moyenne
cout = 'mean_squared_error'
#une metric= fonction qui permet de juger la performance du modele 
model.compile(loss=cout,optimizer=sgd,metrics=['accuracy'])



#APPRENTISSAGE DU MODELE
#epochs = nombre d'iterations
#batch_size = nombre d'exemples par mise a jour du gradient
#validation_split = pourcentage de donnees utilisee pour les tests
#1 epoch = 1 propagation avant et arriere pour tous les exemples d'apprentissage
#batch size =nombre d'exemples d'apprentissage dans une seule propagation avant/arriere. Plus ce chiffre est grand, plus on aura besoin de memoire.
#nombre d'iteration = nombre de propagations, chaque propagation (avant+arriere=1 propagation) utilise [batch size] nombres d'exemples d'apprentissage.
#Exemple:  1000 exemples d'apprentissage et batch size=500 alors il y a 2 iterations pour faire 1 epoch..
#early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=2, verbose = 0)
history = model.fit(x_train, y_train,epochs=100,batch_size=1, verbose=1,shuffle=True ) #, callbacks=[early_stopping])


#courbe de la precision sur les ensembles de donnees d'apprentissage et de validation au cours des iterations d'apprentissage.
plt.plot(history.history['acc'])
#plt.plot(history.history['val_acc'])
plt.title('Precision du modele')
plt.ylabel('Precision')
plt.xlabel('Iterations')
plt.legend(['Apprentissage', 'Test'], loc='upper left')
plt.show()
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
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=1)
print "Loss et metrics ",loss_and_metrics

#PREDICTION
previsions = model.predict(np.array([[-0.0294117647	,-0.0002883506,	0.0092300473]]))
np.savetxt('prediction.txt', previsions)

#sauvegarder le modele
model.save(nomFichierDuModele)






# Chargement du modele stocke dans le fichier pour le reutiliser
model = load_model(nomFichierDuModele)
