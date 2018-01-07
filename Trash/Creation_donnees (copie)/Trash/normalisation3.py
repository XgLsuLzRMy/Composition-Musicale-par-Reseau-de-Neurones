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
	    #event.append(float(s[0]))
	    tick.append(float(s[0]))
	    data1.append(float(s[1]))
	    data2.append(float(s[2]))
    donnees.close()
    
    max_event = 1
    min_event = 0
    max_tick = 155520
    min_tick = 0
    max_data1 = 127
    min_data1 = 0
    max_data2 = max_data1
    min_data2 = min_data1
    for i in range(0,len(tick)):
	    t = Decimal((float(tick[i])-min_tick)/(max_tick- min_tick))
	    if (t==0):
                t=0.0
	    if (t==1):
	        t=1.0
	    mon_fichier.write(str(t)+" ")
	    d1 = Decimal((float(data1[i])-min_data1)/(max_data1- min_data1))
	    if (d1==0):
                d1=0.0
	    if (d1==1):
                d1=1.0
	    mon_fichier.write(str(d1)+" ")
	    d2 = Decimal((float(data2[i])-min_data2)/(max_data2 - min_data2))
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
    if nbLignes>=2000:
        emplacement = "Apprentissage"
        decouper(file,2000,nbLignes)
        os.rename(file, emplacement+"/"+file)
    else:
        if nbLignes in range(400,2000):
            emplacement = "Test"
            decouper(file,400,nbLignes)
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
