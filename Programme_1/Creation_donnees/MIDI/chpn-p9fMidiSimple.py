import midi
pattern=midi.Pattern(format=1, resolution=480, tracks=\
[midi.Track(\
[   midi.NoteOnEvent(tick=1, channel=0, data=[59, 80]),
   midi.NoteOnEvent(tick=479, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 74]),
   midi.NoteOnEvent(tick=400, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 77]),
   midi.NoteOnEvent(tick=80, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 80]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 75]),
   midi.NoteOnEvent(tick=480, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 76]),
   midi.NoteOnEvent(tick=480, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 78]),
   midi.NoteOnEvent(tick=400, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 75]),
   midi.NoteOnEvent(tick=80, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 75]),
   midi.NoteOnEvent(tick=480, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 73]),
   midi.NoteOnEvent(tick=480, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 75]),
   midi.NoteOnEvent(tick=480, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 76]),
   midi.NoteOnEvent(tick=400, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 80]),
   midi.NoteOnEvent(tick=80, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 80]),
   midi.NoteOnEvent(tick=480, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 85]),
   midi.NoteOnEvent(tick=400, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 85]),
   midi.NoteOnEvent(tick=80, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 90]),
   midi.NoteOnEvent(tick=480, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 80]),
   midi.NoteOnEvent(tick=400, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 64]),
   midi.NoteOnEvent(tick=80, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 64]),
   midi.NoteOnEvent(tick=480, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 64]),
   midi.NoteOnEvent(tick=400, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 46]),
   midi.NoteOnEvent(tick=80, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 41]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 44]),
   midi.NoteOnEvent(tick=400, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 47]),
   midi.NoteOnEvent(tick=80, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 47]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 51]),
   midi.NoteOnEvent(tick=400, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 61]),
   midi.NoteOnEvent(tick=80, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 62]),
   midi.NoteOnEvent(tick=480, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 66]),
   midi.NoteOnEvent(tick=480, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 72]),
   midi.NoteOnEvent(tick=480, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 76]),
   midi.NoteOnEvent(tick=400, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 80]),
   midi.NoteOnEvent(tick=80, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 83]),
   midi.NoteOnEvent(tick=480, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 86]),
   midi.NoteOnEvent(tick=400, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 87]),
   midi.NoteOnEvent(tick=80, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[65, 89]),
   midi.NoteOnEvent(tick=480, channel=0, data=[65, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[67, 91]),
   midi.NoteOnEvent(tick=480, channel=0, data=[67, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[68, 96]),
   midi.NoteOnEvent(tick=320, channel=0, data=[68, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 91]),
   midi.NoteOnEvent(tick=160, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 88]),
   midi.NoteOnEvent(tick=400, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 78]),
   midi.NoteOnEvent(tick=80, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 75]),
   midi.NoteOnEvent(tick=400, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 71]),
   midi.NoteOnEvent(tick=80, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 69]),
   midi.NoteOnEvent(tick=400, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 44]),
   midi.NoteOnEvent(tick=80, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 36]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 39]),
   midi.NoteOnEvent(tick=420, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 40]),
   midi.NoteOnEvent(tick=60, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 42]),
   midi.NoteOnEvent(tick=480, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 45]),
   midi.NoteOnEvent(tick=480, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 49]),
   midi.NoteOnEvent(tick=480, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 42]),
   midi.NoteOnEvent(tick=420, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 45]),
   midi.NoteOnEvent(tick=60, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 46]),
   midi.NoteOnEvent(tick=480, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 62]),
   midi.NoteOnEvent(tick=400, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 70]),
   midi.NoteOnEvent(tick=80, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 61]),
   midi.NoteOnEvent(tick=480, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 74]),
   midi.NoteOnEvent(tick=420, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 73]),
   midi.NoteOnEvent(tick=60, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[62, 73]),
   midi.NoteOnEvent(tick=480, channel=0, data=[62, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[63, 84]),
   midi.NoteOnEvent(tick=420, channel=0, data=[63, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 82]),
   midi.NoteOnEvent(tick=60, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 89]),
   midi.NoteOnEvent(tick=480, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 88]),
   midi.NoteOnEvent(tick=420, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 87]),
   midi.NoteOnEvent(tick=60, channel=0, data=[64, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[64, 94]),
   midi.NoteOnEvent(tick=960, channel=0, data=[64, 0]),
   midi.EndOfTrackEvent(tick=0, data=[])]),
 midi.Track(\
[    midi.NoteOnEvent(tick=4, channel=0, data=[52, 49]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 58]),
   midi.NoteOnEvent(tick=156, channel=0, data=[47, 52]),
   midi.NoteOnEvent(tick=4, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=156, channel=0, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 39]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 48]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 45]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 54]),
   midi.NoteOnEvent(tick=160, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 51]),
   midi.NoteOnEvent(tick=160, channel=0, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 38]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 45]),
   midi.NoteOnEvent(tick=160, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 50]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 46]),
   midi.NoteOnEvent(tick=160, channel=0, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 33]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 40]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 50]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 59]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[49, 46]),
   midi.NoteOnEvent(tick=160, channel=0, data=[49, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 34]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 54]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 64]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[49, 45]),
   midi.NoteOnEvent(tick=160, channel=0, data=[49, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 36]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 43]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 52]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 61]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[49, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[49, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 31]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 50]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 34]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 50]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 44]),
   midi.NoteOnEvent(tick=160, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 37]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 44]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 48]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 57]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 48]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 37]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 44]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 60]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 51]),
   midi.NoteOnEvent(tick=160, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 45]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 36]),
   midi.NoteOnEvent(tick=160, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 64]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 54]),
   midi.NoteOnEvent(tick=160, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 45]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 64]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 54]),
   midi.NoteOnEvent(tick=160, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 45]),
   midi.NoteOnEvent(tick=160, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 49]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 59]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 70]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 49]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 38]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 46]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 54]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 64]),
   midi.NoteOnEvent(tick=160, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 45]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 34]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 42]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 50]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[49, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[49, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 34]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 51]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 28]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 33]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 27]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 32]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 25]),
   midi.NoteOnEvent(tick=160, channel=0, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 21]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 25]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 28]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 34]),
   midi.NoteOnEvent(tick=160, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 27]),
   midi.NoteOnEvent(tick=160, channel=0, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 22]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 27]),
   midi.NoteOnEvent(tick=160, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 29]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 34]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 28]),
   midi.NoteOnEvent(tick=160, channel=0, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 22]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 27]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 34]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 40]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 30]),
   midi.NoteOnEvent(tick=160, channel=0, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 24]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 30]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 49]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 40]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 40]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 52]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 44]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 43]),
   midi.NoteOnEvent(tick=160, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 43]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 56]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 47]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 46]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 48]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 58]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 49]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 52]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 50]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 42]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 54]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 65]),
   midi.NoteOnEvent(tick=160, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 58]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 53]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 45]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 56]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 66]),
   midi.NoteOnEvent(tick=160, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 58]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 46]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 54]),
   midi.NoteOnEvent(tick=160, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 59]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 70]),
   midi.NoteOnEvent(tick=160, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 59]),
   midi.NoteOnEvent(tick=160, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 46]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 55]),
   midi.NoteOnEvent(tick=160, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 60]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 71]),
   midi.NoteOnEvent(tick=160, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 61]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 47]),
   midi.NoteOnEvent(tick=0, channel=0, data=[61, 56]),
   midi.NoteOnEvent(tick=160, channel=0, data=[61, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 60]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 72]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 62]),
   midi.NoteOnEvent(tick=160, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 48]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 57]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 60]),
   midi.NoteOnEvent(tick=0, channel=0, data=[60, 72]),
   midi.NoteOnEvent(tick=160, channel=0, data=[60, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 57]),
   midi.NoteOnEvent(tick=160, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 48]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 57]),
   midi.NoteOnEvent(tick=160, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 63]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 45]),
   midi.NoteOnEvent(tick=160, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 45]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 45]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 54]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 33]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 24]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 28]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 21]),
   midi.NoteOnEvent(tick=160, channel=0, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 19]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 22]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 24]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 30]),
   midi.NoteOnEvent(tick=160, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 19]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 29]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 34]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[47, 25]),
   midi.NoteOnEvent(tick=160, channel=0, data=[47, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 21]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 25]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 30]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 36]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 25]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 31]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 33]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 27]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 24]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 28]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 25]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 29]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 24]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 20]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 25]),
   midi.NoteOnEvent(tick=160, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 31]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 37]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[48, 28]),
   midi.NoteOnEvent(tick=160, channel=0, data=[48, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 25]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 30]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 39]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 47]),
   midi.NoteOnEvent(tick=160, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 39]),
   midi.NoteOnEvent(tick=160, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 30]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 36]),
   midi.NoteOnEvent(tick=160, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[53, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 34]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 56]),
   midi.NoteOnEvent(tick=160, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 46]),
   midi.NoteOnEvent(tick=160, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 36]),
   midi.NoteOnEvent(tick=0, channel=0, data=[58, 51]),
   midi.NoteOnEvent(tick=160, channel=0, data=[58, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 51]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 55]),
   midi.NoteOnEvent(tick=160, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 52]),
   midi.NoteOnEvent(tick=0, channel=0, data=[57, 52]),
   midi.NoteOnEvent(tick=160, channel=0, data=[57, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 51]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 60]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[50, 55]),
   midi.NoteOnEvent(tick=160, channel=0, data=[50, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 39]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 55]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[55, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 42]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 70]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[51, 64]),
   midi.NoteOnEvent(tick=160, channel=0, data=[51, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 42]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 59]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[54, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 54]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 76]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 66]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 50]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 59]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 54]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 76]),
   midi.NoteOnEvent(tick=160, channel=0, data=[59, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 67]),
   midi.NoteOnEvent(tick=160, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 57]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 48]),
   midi.NoteOnEvent(tick=160, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 54]),
   midi.NoteOnEvent(tick=0, channel=0, data=[52, 54]),
   midi.NoteOnEvent(tick=960, channel=0, data=[52, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[56, 0]),
   midi.NoteOnEvent(tick=0, channel=0, data=[59, 0]),
   midi.EndOfTrackEvent(tick=0, data=[])])])
midi.write_midifile("creationMidi.mid", pattern)