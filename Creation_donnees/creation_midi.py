import sys
import re
import subprocess
argument1 = sys.argv[1]
donnees = open(argument1, "r")
mon_fichier = open("new_midi.py", "w")
mon_fichier.write("import midi\npattern=midi.Pattern(format=1, resolution=480, tracks=\\\n[midi.Track(\\\n[")
k=0
for line in donnees :
	s = re.findall(r"[-+]?\d*\.\d+|\d+", line)
	if s[0]=="0":
		event="ControlChangeEvent"	
	else: 
		if s[0]=="0.5":
			event="NoteOnEvent"
		else:
			if s[0]=="1":
				event="EndOfTrackEvent"
				k+=1
	if k==1:
		fin="])]),\n midi.Track(\\\n["
		k+=1
	else:
		if k==3:
			fin="])])])\n"
		else:
			fin = "]),\n"
	note="   midi."+event+"("+"tick="+s[1]+", channel=0, data=["+s[2]+","+s[3] + fin
	mon_fichier.write(note)
		
donnees.close()	
mon_fichier.write('\nmidi.write_midifile("newMusic.mid", pattern)')	
mon_fichier.close()
subprocess.call("python3 new_midi.py", shell=True)
