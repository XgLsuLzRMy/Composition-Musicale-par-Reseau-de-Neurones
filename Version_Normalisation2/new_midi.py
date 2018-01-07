import midi
pattern=midi.Pattern(format=1, resolution=480, tracks=\
[midi.Track(\
[   midi.NoteOnEvent(tick=0, channel=0, data=[71,50]),
   midi.NoteOnEvent(tick=60, channel=0, data=[71,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58,0]),
   midi.NoteOnEvent(tick=60, channel=0, data=[60,41]),
   midi.NoteOnEvent(tick=0, channel=0, data=[73,50]),
   midi.NoteOnEvent(tick=60, channel=0, data=[73,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60,0]),
   midi.NoteOnEvent(tick=60, channel=0, data=[61,41]),
   midi.NoteOnEvent(tick=0, channel=0, data=[73,50]),
   midi.NoteOnEvent(tick=239, channel=0, data=[73,0]),
   midi.NoteOnEvent(tick=82, channel=0, data=[70,27]),
   midi.NoteOnEvent(tick=84, channel=0, data=[71,27]),
   midi.NoteOnEvent(tick=87, channel=0, data=[71,27]),
   midi.NoteOnEvent(tick=92, channel=0, data=[72,27]),
   midi.NoteOnEvent(tick=98, channel=0, data=[73,26]),
   midi.NoteOnEvent(tick=103, channel=0, data=[73,26]),
   midi.NoteOnEvent(tick=108, channel=0, data=[74,26]),
   midi.NoteOnEvent(tick=113, channel=0, data=[74,26]),
   midi.NoteOnEvent(tick=117, channel=0, data=[75,25]),
   midi.NoteOnEvent(tick=120, channel=0, data=[75,25]),
   midi.EndOfTrackEvent(tick=0, channel=0, data=[0,0])])])

midi.write_midifile("newMusic.mid", pattern)