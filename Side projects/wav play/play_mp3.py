import os
from playsound import playsound

morse_code = '...___...'

long_beep = os.path.dirname(__file__) + '\dah.wav'
short_beep = os.path.dirname(__file__) + '\dit.wav'

for character in morse_code:
    if character == '.':
        playsound(long_beep)
    elif character == '_':
        playsound(short_beep)
