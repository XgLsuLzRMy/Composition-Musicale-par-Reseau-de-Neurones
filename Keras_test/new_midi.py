import midi
pattern=midi.Pattern(format=1, resolution=480, tracks=\
[midi.Track(\
[   midi.NoteOnEvent(tick=0, channel=0, data=[79,69]),
   midi.NoteOnEvent(tick=720, channel=0, data=[79,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[75,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74,66]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77,78]),
   midi.NoteOnEvent(tick=240, channel=0, data=[77,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74,68]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77,80]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77,78]),
   midi.NoteOnEvent(tick=240, channel=0, data=[77,0]),
   midi.NoteOnEvent(tick=138, channel=0, data=[107,45]),
   midi.EndOfTrackEvent(tick=0, channel=0, data=[0,0])])])

midi.write_midifile("newMusic.mid", pattern)