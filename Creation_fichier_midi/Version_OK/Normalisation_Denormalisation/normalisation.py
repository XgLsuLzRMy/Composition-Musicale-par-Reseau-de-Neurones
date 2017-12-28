import sys
import re
import subprocess
argument1 = sys.argv[1]
donnees = open(argument1, "r")
mon_fichier = open("donneesNormalises.txt", "w")
	
lines = donnees.readlines()
event = []
tick = []
data1 = []
data2 = []
for line in lines:
	s = re.findall(r"[-+]?\d*\.\d+|\d+", line)
	event.append(s[0])
	tick.append(s[1])
	data1.append(s[2])
	data2.append(s[3])
donnees.close()
#max_event = float(max(event,key=float))
#min_event = float(min(event,key=float))
#max_tick = float(max(tick,key=float)) 
#min_tick = float(min(tick,key=float))
#max_data1 = 127
#min_data1 = 0
#max_data2 = max_data1
#min_data2 = min_data1

max_event = 2
min_event = 0
max_tick = 1700
min_tick = 0
max_data1 = 127
min_data1 = 0
max_data2 = max_data1
min_data2 = min_data1

for i in range(0,len(event)):
        e = (float(event[i])-min_event)/(max_event- min_event)
        mon_fichier.write(str(e)+" ")
        t = (float(tick[i])-min_tick)/(max_tick- min_tick)
        mon_fichier.write(str(t)+" ")
        d1 = (float(data1[i])-min_data1)/(max_data1- min_data1)
        mon_fichier.write(str(d1)+" ")
        d2 = (float(data2[i])-min_data2)/(max_data2 - min_data2)
        mon_fichier.write(str(d2)+"\n")


mon_fichier.close()

