import sys
import re
import subprocess
import os

import numpy as np
import sys
import re
import subprocess
import os
import os.path 

def creationDonnees(file):
			#argument1 = cheminFichierMid
			pos = file.find('.mid')
			nom = file[0:pos]
			print("Traitement du fichier : ",nom)
			nomFichier = subprocess.call("mididump.py "+ file+" > "+ nom+"fMidiComplet.py", shell=True)
			fichier = open(nom+"fMidiComplet.py", "r")
			mon_fichier = open(nom+"fMidiSimple.py", "w")
			mon_fichier2 = open(nom+"MODIF"+"fMidiSimple.py", "w")
			mon_fichier.write("import midi\npattern=")
			k=0		
			ligne=[]
			for line in fichier :
				 ligne.append(line)
			fichier.close()
			i=0
			end = 0
			nbTrack=0
			for i in range(len(ligne)):
				if(i<len(ligne)-2) and end==0:
					if "midi.Track(" in ligne[i] and "midi.TrackNameEvent" in ligne[i+1] and "midi.EndOfTrackEvent(" in ligne[i+2]:
						end=i
				i+=1
			print(end)
			fichier = open(nom+"fMidiComplet.py", "r")
			bad_words = ['PortEvent','EndOfTrackEvent','SmpteOffsetEvent', 'TrackNameEvent', 'TextMetaEvent', 'SetTempoEvent','CopyrightMetaEvent','TimeSignatureEvent','KeySignatureEvent','ProgramChangeEvent','MarkerEvent']
			nombreTrack = 0
			fin = 1
			for line in fichier :
				 if 'midi.Track(' in line :
					 nombreTrack+=1
			fichier.close()
			fichier = open(nom+"fMidiComplet.py", "r")
			index=0
			for line in fichier :
				 clean = True
				 if 'midi.Track(' in line:
					 k+=1
				 for word in bad_words :
				     if word in line:
				         clean = False
				 if clean == True and k<=4:
						if 'midi.Track(' in line:
							if k==2:
								mon_fichier.write("[midi.Track(\\\n[")
							if k==3:
								mon_fichier.write('   midi.EndOfTrackEvent(tick=0, data=[])]),\n midi.Track(\\\n[ ')
							if k==4:
								mon_fichier.write('   midi.EndOfTrackEvent(tick=0, data=[])])])')	
						else: mon_fichier.write(line) 
				 if k>4 and index<=end :
					 if clean == True:
						 if 'midi.Track(' in line :
								if k==5:
									mon_fichier2.write("[midi.Track(\\\n[")
								if k==6:
									mon_fichier2.write('   midi.EndOfTrackEvent(tick=0, data=[])]),\n midi.Track(\\\n[ ')
								if k==7:
									mon_fichier2.write('   midi.EndOfTrackEvent(tick=0, data=[])])])')	
						 else: mon_fichier2.write(line) 
				 index+=1
			mon_fichier.write('\nmidi.write_midifile("creationMidi.mid", pattern)')	
			mon_fichier.close()		
			mon_fichier2.close()	
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
				if k=="0" or k=="0.5":
					s = re.findall(r"[-+]?\d*\.\d+|\d+", line)
					donnees.write(k)
					donnees.write(" "+s[0])
					donnees.write(" "+s[2])
					donnees.write(" "+s[3])
					donnees.write("\n")
				if k=="1":
					donnees.write(k+" 0"+" 0"+" 0\n")
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


	
