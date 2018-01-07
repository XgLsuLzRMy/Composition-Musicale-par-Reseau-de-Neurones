import sys
import re
import subprocess
import os
import sys
import re
import subprocess
import os,glob
import os.path 
from decimal import Decimal
import numpy as np
max_ligne = 2000
min_ligne = 440
max_tick = 3800
min_tick = 0
max_data1 = 127
min_data1 = 0
max_data2 = max_data1
min_data2 = min_data1

mean_tick = 84.15
std_tick = 168.49
mean_data1 = 70.42
std_data1 = 10.16
mean_data2 = 26.55 
std_data2 = 28.88
def tanhEstimators(x,moyenne,ecartType):
    return float(0.5*(np.tanh(0.01*(x-moyenne)/ecartType)+1))


def normalisation(file):
    print("Normalisation du fichier: ",file)
    pos = file.find('.mid')
    nom = file[0:pos]
    donnees = open(file, "r")
    os.chdir(os.path.dirname(os.getcwd()))
    os.chdir('DonneesNormalisees')
    mon_fichier = open(nom+".txt", "w")
	    
    lines = donnees.readlines()
    event = []
    tick = []
    data1 = []
    data2 = []
    for line in lines:
	    s = re.findall(r"[-+]?\d*\.\d+|\d+", line)
	    if float(s[0])<=max_tick:
                tick.append(float(s[0]))
                data1.append(float(s[1]))
                data2.append(float(s[2]))
    donnees.close()

    for i in range(0,len(tick)):
	    t = Decimal(tanhEstimators(float(tick[i]),mean_tick,std_tick))
	    if (t==0):
                t=0.0
	    if (t==1):
	        t=1.0
	    mon_fichier.write(str(t)+" ")
	    d1 = Decimal(tanhEstimators(float(data1[i]),mean_data1,std_data1))
	    if (d1==0):
                d1=0.0
	    if (d1==1):
                d1=1.0
	    mon_fichier.write(str(d1)+" ")
	    d2 = Decimal(tanhEstimators(float(data2[i]),mean_data2,std_data2))
	    if (d2==0):
                d2=0.0
	    if (d2==1):
                d2=1.0
	    mon_fichier.write(str(d2)+"\n")
	    if (t or d1 or d2)>1.0 or (t or d1 or d2)<0.0:
                print("Probleme de normalisation!")
                print(i)
    
    
    mon_fichier.close()
    os.chdir(os.path.dirname(os.getcwd()))
    os.chdir('Donnees')



#NORMALISATION DES DONNEES
os.chdir('Donnees')
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.txt'):
            normalisation(file)
	    
def decouper(file, taille,nbLignes):
    lines = open(file).readlines()
    if nbLignes!=taille:
        open(file, 'w').writelines(lines[0:taille-1])
        open(file, 'a').write(lines[nbLignes-1])
    else:
        open(file, 'w').writelines(lines[0:taille-1])
        open(file, 'a').write(lines[nbLignes-1])


def deplacer(file):
    print(file)
    fichier = open(file, "r")
    nbLignes=0
    for line in fichier :
             nbLignes+=1
    emplacement = " "
    if nbLignes>=max_ligne:
        emplacement = "Apprentissage"
        decouper(file,max_ligne,nbLignes)
        os.rename(file, emplacement+"/"+file)
    else:
        if nbLignes in range(min_ligne,max_ligne):
            emplacement = "Test"
            decouper(file,min_ligne,nbLignes)
            os.rename(file, emplacement+"/"+file)
    if emplacement!=" ":
        os.chdir(emplacement)
        donnees= open(file,"r")
        lines = donnees.readlines()
        e= []
        nb1=0
        for line in lines:
                s = re.findall(r"[-+]?\d*\.\d+|\d+", line)
                e.append(float(s[0]))
        for element in e:
            if element==1:
                nb1+=1
        if nb1>2:
            print("Erreur", nb1)
        os.chdir(os.path.dirname(os.getcwd()))

#TRI DES FICHIERS POUR APPRENTISSAGE OU TEST
os.chdir(os.path.dirname(os.getcwd()))
os.chdir('DonneesNormalisees')
for file in glob.glob("*.txt"):
        if file.endswith('.txt'):
            deplacer(file)

#CONCATENATION DES FICHIERS POUR APPRENTISSAGE	    
import shutil
os.chdir('Apprentissage')
outfilename="donneesNormalisees.txt"
with open(outfilename, 'wb') as outfile:
    for filename in glob.glob('*.txt'):
        if filename == outfilename:
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
os.chdir(os.path.dirname(os.getcwd()))
os.rename("Apprentissage/"+outfilename, os.getcwd()+"/" +outfilename)


#CONCATENATION DES FICHIERS POUR TEST	    
os.chdir('Test')
outfilename="donneesTest.txt"
with open(outfilename, 'wb') as outfile:
    for filename in glob.glob('*.txt'):
        if filename == outfilename:
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
os.chdir(os.path.dirname(os.getcwd()))
os.rename("Test/"+outfilename, os.getcwd()+"/" +outfilename)
