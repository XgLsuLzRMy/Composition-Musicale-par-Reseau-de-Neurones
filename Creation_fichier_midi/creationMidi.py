import sys
 
argument1 = sys.argv[1]
fichier = open(argument1, "r")
mon_fichier = open("test.py", "w")
mon_fichier.write("import midi\npattern=")
#for line in fichier :
     #if 'SmpteOffsetEvent' not in line and 'TrackNameEvent' not in line and 'TextMetaEvent' not in line and 'SetTempoEvent' not in line and 'CopyrightMetaEvent' not in line:
            #mon_fichier.write(line)
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
