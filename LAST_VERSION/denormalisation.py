import sys
import re
import math
import subprocess
from decimal import Decimal
argument1 = sys.argv[1]
donnees = open(argument1, "r")
mon_fichier = open("donneesDenormalises.txt", "w")
	

max_tick = 3500
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
        t = int(float(tick[i])*(max_tick- min_tick)+min_tick)
        mon_fichier.write(str(t)+" ")
        d1 = int(float(data1[i])*(max_data1- min_data1)+min_data1)
        mon_fichier.write(str(d1)+" ")
        d2 = int(float(data2[i])*(max_data2- min_data2)+min_data2)
        mon_fichier.write(str(d2)+"\n")
        print(str(t)+" "+str(d1)+" "+str(d2))


mon_fichier.close()

