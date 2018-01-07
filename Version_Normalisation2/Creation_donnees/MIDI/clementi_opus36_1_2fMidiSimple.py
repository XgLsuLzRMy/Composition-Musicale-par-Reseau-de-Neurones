import midi
pattern=midi.Pattern(format=1, resolution=480, tracks=\
[midi.Track(\
[   midi.NoteOnEvent(tick=0, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=960, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77, 49]),
   midi.NoteOnEvent(tick=480, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 50]),
   midi.NoteOnEvent(tick=960, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 49]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 44]),
   midi.NoteOnEvent(tick=960, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 33]),
   midi.NoteOnEvent(tick=60, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 30]),
   midi.NoteOnEvent(tick=60, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 35]),
   midi.NoteOnEvent(tick=60, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 32]),
   midi.NoteOnEvent(tick=60, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 39]),
   midi.NoteOnEvent(tick=40, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 33]),
   midi.NoteOnEvent(tick=40, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 38]),
   midi.NoteOnEvent(tick=40, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 35]),
   midi.NoteOnEvent(tick=30, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 39]),
   midi.NoteOnEvent(tick=30, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 34]),
   midi.NoteOnEvent(tick=30, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 34]),
   midi.NoteOnEvent(tick=30, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 49]),
   midi.NoteOnEvent(tick=480, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 34]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77, 42]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 39]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 35]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 49]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 34]),
   midi.NoteOnEvent(tick=160, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77, 42]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 39]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 35]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 49]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[81, 53]),
   midi.NoteOnEvent(tick=160, channel=0, data=[81, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 51]),
   midi.NoteOnEvent(tick=160, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 51]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 46]),
   midi.NoteOnEvent(tick=160, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 47]),
   midi.NoteOnEvent(tick=160, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 57]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 49]),
   midi.NoteOnEvent(tick=160, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 49]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 62]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 53]),
   midi.NoteOnEvent(tick=160, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 51]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 62]),
   midi.NoteOnEvent(tick=360, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 48]),
   midi.NoteOnEvent(tick=120, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 43]),
   midi.NoteOnEvent(tick=480, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77, 51]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 48]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 40]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[77, 48]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 40]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 51]),
   midi.NoteOnEvent(tick=80, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[76, 45]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 38]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[76, 45]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 38]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[71, 36]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 43]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[71, 42]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 50]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[71, 45]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 54]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[79, 67]),
   midi.NoteOnEvent(tick=480, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 51]),
   midi.NoteOnEvent(tick=160, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 48]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 48]),
   midi.NoteOnEvent(tick=160, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 51]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 47]),
   midi.NoteOnEvent(tick=160, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 47]),
   midi.NoteOnEvent(tick=160, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 51]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77, 47]),
   midi.NoteOnEvent(tick=160, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 46]),
   midi.NoteOnEvent(tick=160, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 55]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 46]),
   midi.NoteOnEvent(tick=80, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 48]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 40]),
   midi.NoteOnEvent(tick=80, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 46]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 39]),
   midi.NoteOnEvent(tick=80, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[71, 54]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 45]),
   midi.NoteOnEvent(tick=80, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[71, 46]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 39]),
   midi.NoteOnEvent(tick=80, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[71, 46]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 39]),
   midi.NoteOnEvent(tick=80, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 58]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 49]),
   midi.NoteOnEvent(tick=960, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 38]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 45]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 43]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 45]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 49]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[75, 54]),
   midi.NoteOnEvent(tick=160, channel=0, data=[75, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 49]),
   midi.NoteOnEvent(tick=160, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 48]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 43]),
   midi.NoteOnEvent(tick=160, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[66, 47]),
   midi.NoteOnEvent(tick=160, channel=0, data=[66, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 41]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 41]),
   midi.NoteOnEvent(tick=160, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 48]),
   midi.NoteOnEvent(tick=160, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 51]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 43]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 43]),
   midi.NoteOnEvent(tick=160, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 43]),
   midi.NoteOnEvent(tick=144, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=16, channel=0, data=[70, 45]),
   midi.NoteOnEvent(tick=144, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=16, channel=0, data=[70, 49]),
   midi.NoteOnEvent(tick=144, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=22, channel=0, data=[74, 54]),
   midi.NoteOnEvent(tick=154, channel=0, data=[72, 48]),
   midi.NoteOnEvent(tick=6, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=154, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 48]),
   midi.NoteOnEvent(tick=160, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 43]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 47]),
   midi.NoteOnEvent(tick=160, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 41]),
   midi.NoteOnEvent(tick=160, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 41]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 48]),
   midi.NoteOnEvent(tick=160, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 51]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 37]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 43]),
   midi.NoteOnEvent(tick=160, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 35]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 43]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 29]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 35]),
   midi.NoteOnEvent(tick=160, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 36]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 43]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=40, channel=0, data=[69, 36]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 43]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=40, channel=0, data=[69, 39]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 47]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 42]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 35]),
   midi.NoteOnEvent(tick=160, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 41]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 34]),
   midi.NoteOnEvent(tick=160, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 29]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 35]),
   midi.NoteOnEvent(tick=480, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 52]),
   midi.NoteOnEvent(tick=960, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 44]),
   midi.NoteOnEvent(tick=960, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 46]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 54]),
   midi.NoteOnEvent(tick=960, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 33]),
   midi.NoteOnEvent(tick=60, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 30]),
   midi.NoteOnEvent(tick=60, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 36]),
   midi.NoteOnEvent(tick=60, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 33]),
   midi.NoteOnEvent(tick=60, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 41]),
   midi.NoteOnEvent(tick=40, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 35]),
   midi.NoteOnEvent(tick=40, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 41]),
   midi.NoteOnEvent(tick=40, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 38]),
   midi.NoteOnEvent(tick=30, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 43]),
   midi.NoteOnEvent(tick=30, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 38]),
   midi.NoteOnEvent(tick=30, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 38]),
   midi.NoteOnEvent(tick=30, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 35]),
   midi.NoteOnEvent(tick=160, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 34]),
   midi.NoteOnEvent(tick=160, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 42]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 39]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 35]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 43]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 51]),
   midi.NoteOnEvent(tick=80, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[70, 48]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 40]),
   midi.NoteOnEvent(tick=80, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[70, 50]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 42]),
   midi.NoteOnEvent(tick=80, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[65, 46]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 55]),
   midi.NoteOnEvent(tick=80, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[69, 49]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 42]),
   midi.NoteOnEvent(tick=80, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[69, 50]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 42]),
   midi.NoteOnEvent(tick=80, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[64, 36]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 44]),
   midi.NoteOnEvent(tick=80, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[64, 44]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 53]),
   midi.NoteOnEvent(tick=80, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[64, 48]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 58]),
   midi.NoteOnEvent(tick=80, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 73]),
   midi.NoteOnEvent(tick=360, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 58]),
   midi.NoteOnEvent(tick=120, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[77, 71]),
   midi.NoteOnEvent(tick=160, channel=0, data=[77, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 57]),
   midi.NoteOnEvent(tick=160, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 53]),
   midi.NoteOnEvent(tick=160, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 63]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 57]),
   midi.NoteOnEvent(tick=160, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 49]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 65]),
   midi.NoteOnEvent(tick=160, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[70, 57]),
   midi.NoteOnEvent(tick=160, channel=0, data=[70, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 53]),
   midi.NoteOnEvent(tick=160, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 65]),
   midi.NoteOnEvent(tick=480, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 42]),
   midi.NoteOnEvent(tick=60, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 39]),
   midi.NoteOnEvent(tick=60, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 45]),
   midi.NoteOnEvent(tick=60, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 41]),
   midi.NoteOnEvent(tick=60, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 50]),
   midi.NoteOnEvent(tick=40, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 42]),
   midi.NoteOnEvent(tick=40, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 49]),
   midi.NoteOnEvent(tick=40, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 45]),
   midi.NoteOnEvent(tick=30, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 50]),
   midi.NoteOnEvent(tick=30, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 44]),
   midi.NoteOnEvent(tick=30, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 44]),
   midi.NoteOnEvent(tick=30, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 63]),
   midi.NoteOnEvent(tick=1440, channel=0, data=[65, 0]),
   midi.EndOfTrackEvent(tick=0, data=[])]),
 midi.Track(\
[    midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 21]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 21]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=960, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=960, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 23]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 21]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 21]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 37]),
   midi.NoteOnEvent(tick=480, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 40]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 45]),
   midi.NoteOnEvent(tick=480, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 45]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 26]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 26]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 29]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 30]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[43, 40]),
   midi.NoteOnEvent(tick=960, channel=0, data=[43, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 45]),
   midi.NoteOnEvent(tick=480, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 36]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 29]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 29]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 40]),
   midi.NoteOnEvent(tick=960, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 40]),
   midi.NoteOnEvent(tick=480, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 40]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[43, 35]),
   midi.NoteOnEvent(tick=480, channel=0, data=[43, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[36, 40]),
   midi.NoteOnEvent(tick=480, channel=0, data=[36, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[43, 35]),
   midi.NoteOnEvent(tick=480, channel=0, data=[43, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 39]),
   midi.NoteOnEvent(tick=480, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=1440, channel=0, data=[60, 37]),
   midi.NoteOnEvent(tick=480, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 34]),
   midi.NoteOnEvent(tick=480, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 38]),
   midi.NoteOnEvent(tick=480, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=1440, channel=0, data=[58, 37]),
   midi.NoteOnEvent(tick=480, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 34]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 38]),
   midi.NoteOnEvent(tick=480, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 37]),
   midi.NoteOnEvent(tick=480, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[48, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 32]),
   midi.NoteOnEvent(tick=160, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 32]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 35]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 20]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 26]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 22]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 22]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 27]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 23]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 27]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 23]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 25]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 33]),
   midi.NoteOnEvent(tick=960, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[36, 40]),
   midi.NoteOnEvent(tick=960, channel=0, data=[36, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[46, 52]),
   midi.NoteOnEvent(tick=480, channel=0, data=[46, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[45, 45]),
   midi.NoteOnEvent(tick=160, channel=0, data=[45, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[45, 36]),
   midi.NoteOnEvent(tick=160, channel=0, data=[45, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[45, 36]),
   midi.NoteOnEvent(tick=160, channel=0, data=[45, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[46, 36]),
   midi.NoteOnEvent(tick=160, channel=0, data=[46, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 36]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 26]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 26]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[41, 36]),
   midi.NoteOnEvent(tick=160, channel=0, data=[41, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[45, 29]),
   midi.NoteOnEvent(tick=160, channel=0, data=[45, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 29]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 36]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 36]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[45, 36]),
   midi.NoteOnEvent(tick=160, channel=0, data=[45, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[41, 36]),
   midi.NoteOnEvent(tick=480, channel=0, data=[41, 0]),
   midi.EndOfTrackEvent(tick=0, data=[])])])
midi.write_midifile("creationMidi.mid", pattern)