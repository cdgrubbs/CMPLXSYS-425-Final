import os, sys
import random
from amen.utils import example_audio_file
from amen.audio import Audio
from amen.synthesize import synthesize

d = "\\stuff\\music"
print("test")
aud = []
print(os.curdir)
os.chdir(os.curdir + d)
print(os.curdir)
ff = os.listdir(os.curdir)
for f in ff:
    print(f)
    aud.append(Audio(f))
beats = aud[0].timings['beats']
beats.extend(aud[1].timings['beats'])
beats.extend(aud[2].timings['beats'])
print(beats)
random.shuffle(beats)
print(beats)
out1 = synthesize(beats[:((len(beats)//2)-1)])
out2 = synthesize(beats[((len(beats)//2)):])
out1.output('1.wav')
out1.output('2.wav')