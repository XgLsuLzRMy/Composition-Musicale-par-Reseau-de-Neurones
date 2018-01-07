import midi
pattern=midi.Pattern(format=1, resolution=480, tracks=\
[midi.Track(\
[   midi.NoteOnEvent(tick=0, channel=0, data=[67, 48]),
   midi.NoteOnEvent(tick=480, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[69, 50]),
   midi.NoteOnEvent(tick=120, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=240, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 49]),
   midi.NoteOnEvent(tick=240, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 55]),
   midi.NoteOnEvent(tick=240, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 50]),
   midi.NoteOnEvent(tick=240, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 55]),
   midi.NoteOnEvent(tick=160, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[78, 50]),
   midi.NoteOnEvent(tick=160, channel=0, data=[78, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 50]),
   midi.NoteOnEvent(tick=160, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 57]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 59]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 50]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 53]),
   midi.NoteOnEvent(tick=120, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 44]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[83, 64]),
   midi.NoteOnEvent(tick=120, channel=0, data=[83, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[81, 60]),
   midi.NoteOnEvent(tick=120, channel=0, data=[81, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[83, 58]),
   midi.NoteOnEvent(tick=120, channel=0, data=[83, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[84, 60]),
   midi.NoteOnEvent(tick=120, channel=0, data=[84, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[86, 64]),
   midi.NoteOnEvent(tick=240, channel=0, data=[86, 0]),
   midi.NoteOnEvent(tick=720, channel=0, data=[81, 69]),
   midi.NoteOnEvent(tick=160, channel=0, data=[81, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[83, 61]),
   midi.NoteOnEvent(tick=160, channel=0, data=[83, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[81, 61]),
   midi.NoteOnEvent(tick=160, channel=0, data=[81, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[86, 72]),
   midi.NoteOnEvent(tick=160, channel=0, data=[86, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[85, 64]),
   midi.NoteOnEvent(tick=160, channel=0, data=[85, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[83, 64]),
   midi.NoteOnEvent(tick=160, channel=0, data=[83, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[81, 69]),
   midi.NoteOnEvent(tick=160, channel=0, data=[81, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 62]),
   midi.NoteOnEvent(tick=160, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[78, 62]),
   midi.NoteOnEvent(tick=160, channel=0, data=[78, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 69]),
   midi.NoteOnEvent(tick=160, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[83, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[83, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 68]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[73, 66]),
   midi.NoteOnEvent(tick=80, channel=0, data=[73, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 60]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[73, 60]),
   midi.NoteOnEvent(tick=80, channel=0, data=[73, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 64]),
   midi.NoteOnEvent(tick=60, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[73, 52]),
   midi.NoteOnEvent(tick=60, channel=0, data=[73, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 53]),
   midi.NoteOnEvent(tick=60, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[73, 59]),
   midi.NoteOnEvent(tick=60, channel=0, data=[73, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 68]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=960, channel=0, data=[67, 48]),
   midi.NoteOnEvent(tick=480, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[69, 50]),
   midi.NoteOnEvent(tick=120, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=240, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 49]),
   midi.NoteOnEvent(tick=240, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 55]),
   midi.NoteOnEvent(tick=240, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 50]),
   midi.NoteOnEvent(tick=240, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 55]),
   midi.NoteOnEvent(tick=160, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[78, 50]),
   midi.NoteOnEvent(tick=160, channel=0, data=[78, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 50]),
   midi.NoteOnEvent(tick=160, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 57]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 59]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 50]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 53]),
   midi.NoteOnEvent(tick=120, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 44]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[83, 64]),
   midi.NoteOnEvent(tick=120, channel=0, data=[83, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[81, 60]),
   midi.NoteOnEvent(tick=120, channel=0, data=[81, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[83, 58]),
   midi.NoteOnEvent(tick=120, channel=0, data=[83, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[84, 60]),
   midi.NoteOnEvent(tick=120, channel=0, data=[84, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[86, 64]),
   midi.NoteOnEvent(tick=240, channel=0, data=[86, 0]),
   midi.NoteOnEvent(tick=720, channel=0, data=[81, 69]),
   midi.NoteOnEvent(tick=160, channel=0, data=[81, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[83, 61]),
   midi.NoteOnEvent(tick=160, channel=0, data=[83, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[81, 61]),
   midi.NoteOnEvent(tick=160, channel=0, data=[81, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[86, 72]),
   midi.NoteOnEvent(tick=160, channel=0, data=[86, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[85, 64]),
   midi.NoteOnEvent(tick=160, channel=0, data=[85, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[83, 64]),
   midi.NoteOnEvent(tick=160, channel=0, data=[83, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[81, 69]),
   midi.NoteOnEvent(tick=160, channel=0, data=[81, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 62]),
   midi.NoteOnEvent(tick=160, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[78, 62]),
   midi.NoteOnEvent(tick=160, channel=0, data=[78, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 69]),
   midi.NoteOnEvent(tick=160, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[83, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[83, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 68]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[73, 66]),
   midi.NoteOnEvent(tick=80, channel=0, data=[73, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 60]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[73, 60]),
   midi.NoteOnEvent(tick=80, channel=0, data=[73, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 64]),
   midi.NoteOnEvent(tick=60, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[73, 52]),
   midi.NoteOnEvent(tick=60, channel=0, data=[73, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 53]),
   midi.NoteOnEvent(tick=60, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[73, 59]),
   midi.NoteOnEvent(tick=60, channel=0, data=[73, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 68]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=960, channel=0, data=[74, 48]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=240, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 49]),
   midi.NoteOnEvent(tick=240, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 55]),
   midi.NoteOnEvent(tick=240, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 50]),
   midi.NoteOnEvent(tick=240, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 64]),
   midi.NoteOnEvent(tick=160, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[78, 57]),
   midi.NoteOnEvent(tick=160, channel=0, data=[78, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 56]),
   midi.NoteOnEvent(tick=160, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 65]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 59]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 50]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 53]),
   midi.NoteOnEvent(tick=120, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 44]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 64]),
   midi.NoteOnEvent(tick=120, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 60]),
   midi.NoteOnEvent(tick=120, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 58]),
   midi.NoteOnEvent(tick=120, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[78, 60]),
   midi.NoteOnEvent(tick=120, channel=0, data=[78, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 64]),
   midi.NoteOnEvent(tick=240, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 61]),
   midi.NoteOnEvent(tick=120, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=120, channel=0, data=[79, 61]),
   midi.NoteOnEvent(tick=120, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=120, channel=0, data=[79, 61]),
   midi.NoteOnEvent(tick=120, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=120, channel=0, data=[78, 68]),
   midi.NoteOnEvent(tick=120, channel=0, data=[78, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 66]),
   midi.NoteOnEvent(tick=120, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[78, 59]),
   midi.NoteOnEvent(tick=120, channel=0, data=[78, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 65]),
   midi.NoteOnEvent(tick=120, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[81, 69]),
   midi.NoteOnEvent(tick=240, channel=0, data=[81, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 65]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 65]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=120, channel=0, data=[71, 65]),
   midi.NoteOnEvent(tick=120, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=120, channel=0, data=[69, 74]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 68]),
   midi.NoteOnEvent(tick=480, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[66, 66]),
   midi.NoteOnEvent(tick=80, channel=0, data=[66, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 60]),
   midi.NoteOnEvent(tick=80, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[66, 60]),
   midi.NoteOnEvent(tick=80, channel=0, data=[66, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 64]),
   midi.NoteOnEvent(tick=60, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[66, 52]),
   midi.NoteOnEvent(tick=60, channel=0, data=[66, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 53]),
   midi.NoteOnEvent(tick=60, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[66, 59]),
   midi.NoteOnEvent(tick=60, channel=0, data=[66, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 68]),
   midi.NoteOnEvent(tick=960, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 48]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=240, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[69, 49]),
   midi.NoteOnEvent(tick=240, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 55]),
   midi.NoteOnEvent(tick=240, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 50]),
   midi.NoteOnEvent(tick=240, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 64]),
   midi.NoteOnEvent(tick=160, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[78, 57]),
   midi.NoteOnEvent(tick=160, channel=0, data=[78, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 56]),
   midi.NoteOnEvent(tick=160, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 65]),
   midi.NoteOnEvent(tick=480, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 59]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 50]),
   midi.NoteOnEvent(tick=80, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 50]),
   midi.NoteOnEvent(tick=80, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 53]),
   midi.NoteOnEvent(tick=120, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 44]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[71, 50]),
   midi.NoteOnEvent(tick=480, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 64]),
   midi.NoteOnEvent(tick=120, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[74, 60]),
   midi.NoteOnEvent(tick=120, channel=0, data=[74, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 58]),
   midi.NoteOnEvent(tick=120, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[78, 60]),
   midi.NoteOnEvent(tick=120, channel=0, data=[78, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 64]),
   midi.NoteOnEvent(tick=240, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 61]),
   midi.NoteOnEvent(tick=120, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=120, channel=0, data=[79, 61]),
   midi.NoteOnEvent(tick=120, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=120, channel=0, data=[79, 61]),
   midi.NoteOnEvent(tick=120, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=120, channel=0, data=[78, 68]),
   midi.NoteOnEvent(tick=120, channel=0, data=[78, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 66]),
   midi.NoteOnEvent(tick=120, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[78, 59]),
   midi.NoteOnEvent(tick=120, channel=0, data=[78, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[79, 65]),
   midi.NoteOnEvent(tick=120, channel=0, data=[79, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[81, 70]),
   midi.NoteOnEvent(tick=240, channel=0, data=[81, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 65]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 65]),
   midi.NoteOnEvent(tick=120, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=120, channel=0, data=[71, 65]),
   midi.NoteOnEvent(tick=120, channel=0, data=[71, 0]),
   midi.NoteOnEvent(tick=120, channel=0, data=[69, 74]),
   midi.NoteOnEvent(tick=160, channel=0, data=[69, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[72, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[72, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[76, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[76, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 68]),
   midi.NoteOnEvent(tick=480, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[66, 66]),
   midi.NoteOnEvent(tick=80, channel=0, data=[66, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 60]),
   midi.NoteOnEvent(tick=80, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[66, 60]),
   midi.NoteOnEvent(tick=80, channel=0, data=[66, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 64]),
   midi.NoteOnEvent(tick=60, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[66, 52]),
   midi.NoteOnEvent(tick=60, channel=0, data=[66, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 53]),
   midi.NoteOnEvent(tick=60, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[66, 59]),
   midi.NoteOnEvent(tick=60, channel=0, data=[66, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 68]),
   midi.NoteOnEvent(tick=960, channel=0, data=[67, 0]),
   midi.EndOfTrackEvent(tick=0, data=[])]),
 midi.Track(\
[    midi.NoteOnEvent(tick=480, channel=0, data=[55, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[43, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[43, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[54, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 36]),
   midi.NoteOnEvent(tick=480, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=960, channel=0, data=[59, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 35]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 42]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 36]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 43]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 47]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 56]),
   midi.NoteOnEvent(tick=480, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=960, channel=0, data=[67, 58]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 49]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[66, 51]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 43]),
   midi.NoteOnEvent(tick=480, channel=0, data=[66, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 57]),
   midi.NoteOnEvent(tick=480, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=360, channel=0, data=[50, 51]),
   midi.NoteOnEvent(tick=240, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=720, channel=0, data=[55, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[43, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[43, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[54, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 36]),
   midi.NoteOnEvent(tick=480, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=960, channel=0, data=[59, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 35]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 42]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 36]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 43]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 47]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 56]),
   midi.NoteOnEvent(tick=480, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=960, channel=0, data=[67, 58]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 49]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[66, 51]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 43]),
   midi.NoteOnEvent(tick=480, channel=0, data=[66, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 57]),
   midi.NoteOnEvent(tick=480, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=360, channel=0, data=[50, 51]),
   midi.NoteOnEvent(tick=240, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=240, channel=0, data=[59, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 36]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 34]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 35]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 42]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 54]),
   midi.NoteOnEvent(tick=480, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 59]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 57]),
   midi.NoteOnEvent(tick=480, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 59]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 58]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 49]),
   midi.NoteOnEvent(tick=480, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 57]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=360, channel=0, data=[43, 51]),
   midi.NoteOnEvent(tick=240, channel=0, data=[43, 0]),
   midi.NoteOnEvent(tick=240, channel=0, data=[59, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 36]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 34]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 35]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 42]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 54]),
   midi.NoteOnEvent(tick=480, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 59]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 57]),
   midi.NoteOnEvent(tick=480, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 59]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 58]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 49]),
   midi.NoteOnEvent(tick=480, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 57]),
   midi.NoteOnEvent(tick=480, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 45]),
   midi.NoteOnEvent(tick=120, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=360, channel=0, data=[43, 51]),
   midi.NoteOnEvent(tick=480, channel=0, data=[43, 0]),
   midi.EndOfTrackEvent(tick=0, data=[])])])
midi.write_midifile("creationMidi.mid", pattern)