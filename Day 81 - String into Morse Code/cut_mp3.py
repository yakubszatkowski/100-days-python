from pydub import AudioSegment
import pyaudio  # try to play something with it

song = AudioSegment.from_mp3("mp3 files/original_beep.mp3")

long_beep = song[100:400]
short_beep = song[100:300]

long_beep.export("mp3 files/long_beep.mp3", format="mp3")
short_beep.export("mp3 files/short_beep.mp3", format="mp3")


