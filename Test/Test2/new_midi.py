import midi
pattern=midi.Pattern(format=1, resolution=480, tracks=\
[midi.Track(\
[   midi.NoteOnEvent(tick=120, channel=0, data=[74,57]),
   midi.NoteOnEvent(tick=120, channel=0, data=[76,57]),
   midi.NoteOnEvent(tick=20, channel=0, data=[74,0]),
   midi.NoteOnEvent(tick=100, channel=0, data=[78,57]),
   midi.NoteOnEvent(tick=20, channel=0, data=[76,0]),
   midi.NoteOnEvent(tick=100, channel=0, data=[69,60]),
   midi.NoteOnEvent(tick=20, channel=0, data=[78,0]),
   midi.NoteOnEvent(tick=100, channel=0, data=[69,0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[78,57]),
   midi.NoteOnEvent(tick=120, channel=0, data=[76,57]),
   midi.NoteOnEvent(tick=134, channel=0, data=[78,1]),
   midi.NoteOnEvent(tick=29, channel=0, data=[77,30]),
   midi.NoteOnEvent(tick=130, channel=0, data=[78,1]),
   midi.NoteOnEvent(tick=80, channel=0, data=[78,4]),
   midi.NoteOnEvent(tick=65, channel=0, data=[78,7]),
   midi.NoteOnEvent(tick=44, channel=0, data=[77,19]),
   midi.NoteOnEvent(tick=14, channel=0, data=[78,18]),
   midi.NoteOnEvent(tick=113, channel=0, data=[78,2]),
   midi.NoteOnEvent(tick=153, channel=0, data=[78,0]),
   midi.NoteOnEvent(tick=72, channel=0, data=[78,5]),
   midi.NoteOnEvent(tick=43, channel=0, data=[77,19]),
   midi.NoteOnEvent(tick=55, channel=0, data=[78,11]),
   midi.NoteOnEvent(tick=33, channel=0, data=[78,8]),
   midi.NoteOnEvent(tick=87, channel=0, data=[78,3]),
   midi.NoteOnEvent(tick=69, channel=0, data=[78,6]),
   midi.NoteOnEvent(tick=64, channel=0, data=[78,7]),
   midi.NoteOnEvent(tick=56, channel=0, data=[77,10]),
   midi.NoteOnEvent(tick=75, channel=0, data=[78,5]),
   midi.NoteOnEvent(tick=51, channel=0, data=[77,13]),
   midi.NoteOnEvent(tick=83, channel=0, data=[78,4]),
   midi.NoteOnEvent(tick=64, channel=0, data=[78,7]),
   midi.NoteOnEvent(tick=78, channel=0, data=[78,4]),
   midi.NoteOnEvent(tick=49, channel=0, data=[77,13]),
   midi.NoteOnEvent(tick=64, channel=0, data=[78,9]),
   midi.NoteOnEvent(tick=87, channel=0, data=[78,3]),
   midi.NoteOnEvent(tick=75, channel=0, data=[78,5]),
   midi.NoteOnEvent(tick=45, channel=0, data=[77,16]),
   midi.NoteOnEvent(tick=101, channel=0, data=[78,2]),
   midi.NoteOnEvent(tick=46, channel=0, data=[77,15]),
   midi.NoteOnEvent(tick=150, channel=0, data=[78,0]),
   midi.NoteOnEvent(tick=72, channel=0, data=[78,5]),
   midi.NoteOnEvent(tick=40, channel=0, data=[77,24]),
   midi.NoteOnEvent(tick=80, channel=0, data=[78,5]),
   midi.NoteOnEvent(tick=52, channel=0, data=[77,12]),
   midi.NoteOnEvent(tick=77, channel=0, data=[78,5]),
   midi.NoteOnEvent(tick=84, channel=0, data=[78,3]),
   midi.NoteOnEvent(tick=45, channel=0, data=[77,15]),
   midi.NoteOnEvent(tick=115, channel=0, data=[78,1]),
   midi.NoteOnEvent(tick=58, channel=0, data=[77,9]),
   midi.NoteOnEvent(tick=67, channel=0, data=[78,6]),
   midi.NoteOnEvent(tick=64, channel=0, data=[78,7]),
   midi.NoteOnEvent(tick=50, channel=0, data=[77,13]),
   midi.NoteOnEvent(tick=115, channel=0, data=[78,1]),
   midi.NoteOnEvent(tick=79, channel=0, data=[78,4]),
   midi.NoteOnEvent(tick=49, channel=0, data=[77,13]),
   midi.NoteOnEvent(tick=85, channel=0, data=[78,4]),
   midi.NoteOnEvent(tick=47, channel=0, data=[77,15]),
   midi.NoteOnEvent(tick=98, channel=0, data=[78,2]),
   midi.NoteOnEvent(tick=76, channel=0, data=[78,4]),
   midi.NoteOnEvent(tick=46, channel=0, data=[77,15]),
   midi.NoteOnEvent(tick=92, channel=0, data=[78,3]),
   midi.EndOfTrackEvent(tick=0, channel=0, data=[0,0])])])

midi.write_midifile("newMusic.mid", pattern)