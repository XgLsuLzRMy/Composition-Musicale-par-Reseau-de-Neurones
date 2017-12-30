import midi
pattern=midi.Pattern(format=1, resolution=480, tracks=\
[midi.Track(\
[   midi.ControlChangeEvent(tick=0, channel=0, data=[7,100]),
   midi.ControlChangeEvent(tick=0, channel=0, data=[10,64]),
   midi.ControlChangeEvent(tick=0, channel=0, data=[91,127]),
   midi.NoteOnEvent(tick=960, channel=0, data=[67,49]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59,41]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65,41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[65,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59,43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67,51]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65,43]),
   midi.NoteOnEvent(tick=360, channel=0, data=[65,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67,46]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59,39]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65,39]),
   midi.NoteOnEvent(tick=120, channel=0, data=[65,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60,46]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65,46]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69,55]),
   midi.NoteOnEvent(tick=960, channel=0, data=[69,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71,58]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65,49]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62,49]),
   midi.NoteOnEvent(tick=480, channel=0, data=[62,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62,48]),
   midi.EndOfTrackEvent(tick=172, channel=0, data=[102,44])]),
 midi.Track(\
[   midi.EndOfTrackEvent(tick=166, channel=0, data=[102,44])])])

midi.write_midifile("newMusic.mid", pattern)