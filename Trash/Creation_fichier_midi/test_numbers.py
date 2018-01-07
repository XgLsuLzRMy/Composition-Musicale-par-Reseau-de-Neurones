import re

string = "midi.NoteOnEvent(tick=0, channel=0, data=[81, 39]),"

s = re.findall(r"[-+]?\d*\.\d+|\d+", string)

print(s)
