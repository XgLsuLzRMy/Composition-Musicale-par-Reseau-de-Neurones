import sys
import re
import subprocess
import os


import sys
import re
import subprocess
import os
import os.path 

def creationDonnees(file):
			#nom du fichier
			pos = file.find('.mid')
			nom = file[0:pos]
			print("Traitement du fichier : ",nom)
			#creation du script MIDI complet
			nomFichier = subprocess.call("mididump.py "+ file+" > "+ nom+"fMidiComplet.py", shell=True)
			#creation du script MIDI simplifie
			fichier = open(nom+"fMidiComplet.py", "r")
			mon_fichier = open(nom+"fMidiSimple.py", "w")
			mon_fichier.write("import midi\npattern=")
			k=0
			bad_words = ['ControlChangeEvent','PortEvent','EndOfTrackEvent','SmpteOffsetEvent', 'TrackNameEvent', 'TextMetaEvent', 'SetTempoEvent','CopyrightMetaEvent','TimeSignatureEvent','KeySignatureEvent','ProgramChangeEvent','MarkerEvent']
			nombreTrack = 0
			ligne=[]
			for line in fichier :
				 ligne.append(line)
			fichier.close()
			end = 0
			nbTrack=0
			for i in range(len(ligne)):
				if "midi.Track(" in ligne[i]:
					nbTrack+=1
					if(i<len(ligne)-3) and end==0:
						if "PortEvent" in ligne[i+1] and  "midi.TrackNameEvent" in ligne[i+2] and  "midi.EndOfTrackEvent" in ligne[i+3]:
							end=nbTrack
						else: 
							if "TrackNameEvent" in ligne[i+1] and  "midi.EndOfTrackEvent" in ligne[i+2]:
								end=nbTrack
			print(end)
			fichier.close()
			fichier = open(nom+"fMidiComplet.py", "r")
			for line in fichier :
				 clean = True
				 if 'midi.Track(' in line :
					 k+=1
				 for word in bad_words :
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
								print(k)
						else:
							if (k<4): 
								mon_fichier.write(line)
			mon_fichier.write('\nmidi.write_midifile("creationMidi.mid", pattern)')	
			mon_fichier.close()
			mon_fichier = open(nom+"fMidiSimple.py","r")
			k=-1
			os.chdir(os.path.dirname(os.getcwd()))
			os.chdir('Donnees')
			donnees = open(nom+".txt", "w")
			for line in mon_fichier :
				if 'ControlChangeEvent' in line:
					k="0"
				else: 
					if 'NoteOnEvent' in line: 
						k="0.5"
					else:
						if 'EndOfTrackEvent' in line: 
							k="1"
						else: k=-1
				if k=="0.5":
					s = re.findall(r"[-+]?\d*\.\d+|\d+", line)
					#donnees.write(k)
					donnees.write(s[0])
					donnees.write(" "+s[2])
					donnees.write(" "+s[3])
					donnees.write("\n")
			donnees.close()	
			mon_fichier.close()
			os.chdir(os.path.dirname(os.getcwd()))
			os.chdir('MIDI')
			#os.remove(nom+"fMidiSimple.py")
			#os.remove(nom+"fMidiComplet.py")

os.chdir('MIDI')
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.mid'):
            creationDonnees(file)


	
