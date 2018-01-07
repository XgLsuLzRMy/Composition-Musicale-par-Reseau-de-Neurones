import sys
import re
import subprocess
import os
import numpy as np
import statistics as stats
import sys
import re
import subprocess
import os
import os.path 

max_ligne = 2000
min_ligne = 440
max_tick = 3800


def lecture(file):
        global nbLignesSup3500,nbLignesInf3500,nbLignesSupTICK,nbLignesInfTICK
        print("Lecture du fichier: ", file)
        fichier = open(file, "r")
        nbLignes=0
        for line in fichier :
             s = re.findall(r"[-+]?\d*\.\d+|\d+", line)
             tick.append(float(s[0]))
             data1.append(float(s[1]))
             data2.append(float(s[2]))
             nbLignes+=1
        liste.append(nbLignes)
        if nbLignes>=max_ligne:
            nbLignesSup3500+=1
        if nbLignes<max_ligne and nbLignes>=min_ligne:
            nbLignesInf3500+=1
        if nbLignes>=max_ligne and float(s[0]) <=max_tick:
            nbLignesSupTICK+=1
        if nbLignes<max_ligne and float(s[0]) <= max_tick:
            nbLignesInfTICK+=1


nbLignesSup3500=0
nbLignesInf3500=0
nbLignesSupTICK=0
nbLignesInfTICK=0
nbTickSup=0
nbTickInf=0
event = []
tick = []
data1 = []
data2 = []

os.chdir('Apprentissage')
liste=[]
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.txt'):
            lecture(file)

for element in tick:
    if element > max_tick:
        nbTickSup+=1
    if element <=max_tick:
        nbTickInf+=1


print('\n')
print("Maximum lignes = ",max(liste))
print("Minimim lignes = ",min(liste))
print("Moyenne lignes = ",int(np.mean(liste)))
print("Mediane lignes = ",int(np.median(liste)))
print("Mediane groupe lignes = ",stats.median_grouped(liste))
print("Nombre de lignes > 1500 = ",nbLignesSup3500)
print("Nombre de lignes < 1500 = ",nbLignesInf3500)
print("Nombre de lignes  et tick > = ",nbLignesSupTICK)
print("Nombre de lignes  et tick < = ",nbLignesInfTICK)
#print( list(sorted(set(liste))))


print('\n')
print("Maximum tick = ",max(tick))
print("Minimim tick = ",min(tick))
print("Moyenne tick = ",np.mean(tick))
print("Mediane tick = ",np.median(tick))
print("Ecart type tick = ",np.std(tick))
print("Nb Sup tick = ",nbTickSup)
print("Nb Inf tick = ",nbTickInf)

print('\n')
print("Maximum data1 = ",max(data1))
print("Minimim data1 = ",min(data1))
print("Moyenne data1 = ",np.mean(data1))
print("Mediane data1 = ",np.median(data1))
print("Ecart type data1 = ",np.std(data1))

print('\n')
print("Maximum data2 = ",max(data2))
print("Minimim data2 = ",min(data2))
print("Moyenne data2 = ",np.mean(data2))
print("Mediane data2 = ",np.median(data2))
print("Ecart type data2 = ",np.std(data2))
#from collections import Counter
#print(Counter(liste))

