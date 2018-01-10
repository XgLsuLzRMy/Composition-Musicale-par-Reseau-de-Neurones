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
			#ajout des lignes du fichier dans un tableau
			for line in fichier :
				 ligne.append(line)
			fichier.close()
			fichier = open(nom+"fMidiComplet.py", "r")
			#creation du script complet
			for line in fichier :
				 clean = True
				 if 'midi.Track(' in line :
					 k+=1
				 for word in bad_words :
				     if word in line:
				         clean = False
				 if clean == True:  #si la ligne ne contient pas un mot non souhaite
						if 'midi.Track(' in line:
							if k==2:
								mon_fichier.write("[midi.Track(\\\n[")
							if k==3:
								mon_fichier.write('   midi.EndOfTrackEvent(tick=0, data=[])]),\n midi.Track(\\\n[ ')
							if k==4:
								mon_fichier.write('   midi.EndOfTrackEvent(tick=0, data=[])])])')
						else:
							if (k<4): 
								mon_fichier.write(line)
			mon_fichier.write('\nmidi.write_midifile("creationMidi.mid", pattern)')	
			mon_fichier.close()
			mon_fichier = open(nom+"fMidiSimple.py","r")
			os.chdir(os.path.dirname(os.getcwd()))
			os.chdir('Donnees')
			donnees = open(nom+".txt", "w")
			#creation du script simplifie
			for line in mon_fichier :
					if 'NoteOnEvent' in line: 
						s = re.findall(r"[-+]?\d*\.\d+|\d+", line)
						donnees.write(s[0])
						donnees.write(" "+s[2])
						donnees.write(" "+s[3])
						donnees.write("\n")
			donnees.close()	
			mon_fichier.close()
			os.chdir(os.path.dirname(os.getcwd()))
			os.chdir('MIDI')

os.chdir('MIDI')
#recherche de tous les fichiers MIDI
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('.mid'):
            creationDonnees(file)

	
