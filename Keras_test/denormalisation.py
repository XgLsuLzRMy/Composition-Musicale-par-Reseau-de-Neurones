import sys
import re
import math
import subprocess
argument1 = sys.argv[1]
donnees = open(argument1, "r")
mon_fichier = open("donneesDenormalises.txt", "w")
	
def arrondis(e):
	if e<0.20 :
		 e=0
	else:
		if e>=0.20 and e<0.9:
			e=0.5
		else:
			e=1
	return e

max_tick = 663120
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
	event.append(s[0])
	tick.append(s[1])
	data1.append(s[2])
	data2.append(s[3])
donnees.close()


for i in range(0,len(event)):
        e = arrondis(float(event[i]))
        mon_fichier.write(str(e)+" ")
        t = int(float(tick[i])*(max_tick- min_tick)+min_tick)
        mon_fichier.write(str(t)+" ")
        d1 = int(float(data1[i])*(max_data1- min_data1)+min_data1)
        mon_fichier.write(str(d1)+" ")
        d2 = int(float(data2[i])*(max_data2- min_data2)+min_data2)
        mon_fichier.write(str(d2)+"\n")
        print(str(e)+" "+str(t)+" "+str(d1)+" "+str(d2))


mon_fichier.close()

