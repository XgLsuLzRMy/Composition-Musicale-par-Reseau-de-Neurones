import midi

# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = midi.Pattern()
# Instantiate a MIDI Track (contains a list of MIDI events)
track = midi.Track()
# Append the track to the pattern
pattern.append(track)
# Instantiate a MIDI note on event, append it to the track
on = midi.NoteOnEvent(tick=0, velocity=20, pitch=midi.G_3)
track.append(on)
# Instantiate a MIDI note off event, append it to the track
off = midi.NoteOffEvent(tick=100, pitch=midi.G_3)
track.append(off)
# Add the end of track event, append it to the track
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)
# Print out the pattern
print pattern
# Save the pattern to disk
midi.write_midifile("example.mid", pattern)



#from midiutil.MidiFile import MIDIFile
## create your MIDI object
#mf = MIDIFile(1)     # only 1 track
#track = 0   # the only track
#time = 0    # start at the beginning
#mf.addTrackName(track, time, "Sample Track")
#mf.addTempo(track, time, 120)
## add some notes
#channel = 0
#volume = 100
#pitch = 60           # C4 (middle C)
#time = 0             # start on beat 0
#duration = 1         # 1 beat long
#mf.addNote(track, channel, pitch, time, duration, volume)

#pitch = 64           # E4
#time = 2             # start on beat 2
#duration = 1         # 1 beat long
#mf.addNote(track, channel, pitch, time, duration, volume)

#pitch = 67           # G4
#time = 4             # start on beat 4
#duration = 1         # 1 beat long
#mf.addNote(track, channel, pitch, time, duration, volume)



#mf.addNote(track, channel, 44, 3, 1, volume)

#mf.addNote(track, channel, 50, 6, 1, volume)
## write it to disk
#with open("essais.mid", 'wb') as outf:
    #mf.writeFile(outf)
