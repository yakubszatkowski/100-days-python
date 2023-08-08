from pydub import AudioSegment

song = AudioSegment.from_mp3("original_beep.mp3")

long_beep = song[100:400]
short_beep = song[100:200]

long_beep.export("long_beep.mp3", format="mp3")
short_beep.export("/short_beep.mp3", format="mp3")


