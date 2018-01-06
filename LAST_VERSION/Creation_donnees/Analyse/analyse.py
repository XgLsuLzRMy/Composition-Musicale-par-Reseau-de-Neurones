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

def lecture(file):
        global nbLignesSup3500,nbLignesInf3500
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
        if nbLignes>=1500:
            nbLignesSup3500+=1
        if nbLignes<1500 and nbLignes>=440:
            nbLignesInf3500+=1


nbLignesSup3500=0
nbLignesInf3500=0
nbTickSup=0
nbTickInf=0
event = []
tick = []
data1 = []
data2 = []
os.chdir(os.path.dirname(os.getcwd()))
os.chdir('Donnees')
liste=[]
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.txt'):
            lecture(file)

for element in tick:
    if element > 3500:
        nbTickSup+=1
    if element <=3500:
        nbTickInf+=1


print('\n')
print("Maximum lignes = ",max(liste))
print("Minimim lignes = ",min(liste))
print("Moyenne lignes = ",int(np.mean(liste)))
print("Mediane lignes = ",int(np.median(liste)))
print("Mediane groupe lignes = ",stats.median_grouped(liste))
print("Nombre de lignes > 1500 = ",nbLignesSup3500)
print("Nombre de lignes < 1500 = ",nbLignesInf3500)
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

print('\n')
print("Maximum data2 = ",max(data2))
print("Minimim data2 = ",min(data2))
print("Moyenne data2 = ",np.mean(data2))
print("Mediane data2 = ",np.median(data2))

#from collections import Counter
#print(Counter(liste))

