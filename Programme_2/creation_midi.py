import sys
import re
import subprocess
argument1 = sys.argv[1]
donnees = open(argument1, "r")
mon_fichier = open("new_midi.py", "w")
mon_fichier.write("import midi\npattern=midi.Pattern(format=1, resolution=480, tracks=\\\n[midi.Track(\\\n[")
for line in donnees :
	s = re.findall(r"[-+]?\d*\.\d+|\d+", line)
	note="   midi."+"NoteOnEvent"+"("+"tick="+s[0]+", channel=0, data=["+s[1]+","+s[2] + "]),\n"
	mon_fichier.write(note)

note="   midi."+"EndOfTrackEvent"+"("+"tick="+"0"+", channel=0, data=["+"0"+","+"0" + "])])])\n"
mon_fichier.write(note)	
donnees.close()	
mon_fichier.write('\nmidi.write_midifile("newMusic.mid", pattern)')	
mon_fichier.close()
subprocess.call("python3 new_midi.py", shell=True)
