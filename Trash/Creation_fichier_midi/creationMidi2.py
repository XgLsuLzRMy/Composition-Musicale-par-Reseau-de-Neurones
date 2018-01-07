import sys
import re
argument1 = sys.argv[1]
fichier = open(argument1, "r")
mon_fichier = open("test.py", "w")
mon_fichier.write("import midi\npattern=")
k=0
bad_words = ['EndOfTrackEvent','SmpteOffsetEvent', 'TrackNameEvent', 'TextMetaEvent', 'SetTempoEvent','CopyrightMetaEvent','TimeSignatureEvent','KeySignatureEvent','ProgramChangeEvent']
for line in fichier :
	clean = True
	if 'midi.Track(' in line:
		k+=1
	for word in bad_words:
		if word in line:
			clean = False
	if clean == True:
		if 'midi.Track(' in line:
			if k==2:
				mon_fichier.write("[midi.Track(\\\n[")
			if k==3:
				mon_fichier.write('   midi.EndOfTrackEvent(tick=0, data=[])]),\n midi.Track(\\\n[ ')
			if k==4:
				mon_fichier.write('   midi.EndOfTrackEvent(tick=0, data=[])])])')	
		else: mon_fichier.write(line)
mon_fichier.write('\nmidi.write_midifile("creationMidi.mid", pattern)')	
mon_fichier.close()
mon_fichier = open("test.py","r")
k=-1
donnees = open("donnees.txt", "w")
for line in mon_fichier :
	if 'ControlChangeEvent' in line:
		k="0"
	else: 
		if 'NoteOnEvent' in line: 
			k="1"
		else:
			if 'EndOfTrackEvent' in line: 
				k="2"
			else: k=-1
	if k=="0" or k=="1":
		s = re.findall(r"[-+]?\d*\.\d+|\d+", line)
		donnees.write(k)
		donnees.write(" "+s[0])
		donnees.write(" "+s[2])
		donnees.write(" "+s[3])
		donnees.write("\n")
	if k=="2":
		donnees.write(k+" 0"+" 0"+" 0\n")
		

donnees.close()	
mon_fichier.close()
