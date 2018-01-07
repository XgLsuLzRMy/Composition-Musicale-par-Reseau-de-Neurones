import midi
pattern=midi.Pattern(format=1, resolution=480, tracks=\
[midi.Track(\
[   midi.NoteOnEvent(tick=130, channel=0, data=[74,57]),
   midi.NoteOnEvent(tick=130, channel=0, data=[76,57]),
   midi.NoteOnEvent(tick=21, channel=0, data=[74,0]),
   midi.NoteOnEvent(tick=108, channel=0, data=[78,57]),
   midi.NoteOnEvent(tick=21, channel=0, data=[76,0]),
   midi.NoteOnEvent(tick=108, channel=0, data=[69,60]),
   midi.NoteOnEvent(tick=21, channel=0, data=[78,0]),
   midi.NoteOnEvent(tick=108, channel=0, data=[69,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[78,57]),
   midi.NoteOnEvent(tick=130, channel=0, data=[76,57]),
   midi.NoteOnEvent(tick=463, channel=0, data=[69,28]),
   midi.NoteOnEvent(tick=462, channel=0, data=[69,28]),
   midi.NoteOnEvent(tick=463, channel=0, data=[69,28]),
   midi.NoteOnEvent(tick=465, channel=0, data=[69,28]),
   midi.NoteOnEvent(tick=466, channel=0, data=[69,28]),
   midi.NoteOnEvent(tick=469, channel=0, data=[69,27]),
   midi.NoteOnEvent(tick=471, channel=0, data=[69,27]),
   midi.NoteOnEvent(tick=473, channel=0, data=[69,28]),
   midi.NoteOnEvent(tick=475, channel=0, data=[69,28]),
   midi.NoteOnEvent(tick=477, channel=0, data=[68,28]),
   midi.EndOfTrackEvent(tick=0, channel=0, data=[0,0])])])

midi.write_midifile("newMusic.mid", pattern)