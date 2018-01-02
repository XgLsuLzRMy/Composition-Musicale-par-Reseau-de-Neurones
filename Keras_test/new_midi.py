import midi
pattern=midi.Pattern(format=1, resolution=480, tracks=\
[midi.Track(\
[   midi.ControlChangeEvent(tick=0, channel=0, data=[7,100]),
   midi.ControlChangeEvent(tick=0, channel=0, data=[64,0]),
   midi.ControlChangeEvent(tick=0, channel=0, data=[91,127]),
   midi.NoteOnEvent(tick=480, channel=0, data=[56,34]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54,28]),
   midi.NoteOnEvent(tick=240, channel=0, data=[54,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56,0]),
   midi.NoteOnEvent(tick=240, channel=0, data=[54,28]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56,34]),
   midi.NoteOnEvent(tick=240, channel=0, data=[56,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54,0]),
   midi.NoteOnEvent(tick=720, channel=0, data=[61,33]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65,39]),
   midi.NoteOnEvent(tick=240, channel=0, data=[65,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61,0]),
   midi.NoteOnEvent(tick=240, channel=0, data=[61,35]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65,41]),
   midi.NoteOnEvent(tick=240, channel=0, data=[65,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61,0]),
   midi.NoteOnEvent(tick=720, channel=0, data=[68,40]),
   midi.NoteOnEvent(tick=30561, channel=0, data=[69,27]),
   midi.NoteOnEvent(tick=30521, channel=0, data=[69,27]),
   midi.NoteOnEvent(tick=30468, channel=0, data=[69,27]),
   midi.EndOfTrackEvent(tick=0, channel=0, data=[0,0])])])

midi.write_midifile("newMusic.mid", pattern)