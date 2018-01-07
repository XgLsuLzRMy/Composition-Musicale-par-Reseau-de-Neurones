import sys
import re
import math
import subprocess
from decimal import Decimal
import numpy as np
argument1 = sys.argv[1]
donnees = open(argument1, "r")
mon_fichier = open("donneesDenormalises.txt", "w")
	


mean_tick = 84.15
std_tick = 168.49
mean_data1 = 70.42
std_data1 = 10.16
mean_data2 = 26.55 
std_data2 = 28.88
def tanhEstimatorsInverse(x,moyenne,ecartType):
    return ecartType*(np.arctanh(2*float(x)-1))/0.01+moyenne



max_ligne = 2000
min_ligne = 440
max_tick = 3800
min_tick = 0
max_data1 = 127
min_data1 = 0
max_data2 = max_data1
min_data2 = min_data1
	
lines = donnees.readlines()
event = []
tick = []
data1 = []
data2 = []
for line in lines:
	s = re.findall(r"[-+]?\d*\.\d+|\d+\t\n\r\f\v", line)
	tick.append(s[0])
	data1.append(s[1])
	data2.append(s[2])
donnees.close()


for i in range(0,len(tick)):
        t = int(tanhEstimatorsInverse(tick[i],mean_tick,std_tick))
        mon_fichier.write(str(t)+" ")
        d1 = int(tanhEstimatorsInverse(data1[i],mean_data1,std_data1))
        mon_fichier.write(str(d1)+" ")
        d2 = int(tanhEstimatorsInverse(data2[i],mean_data2,std_data2))
        mon_fichier.write(str(d2)+"\n")
        print(str(t)+" "+str(d1)+" "+str(d2))


mon_fichier.close()

