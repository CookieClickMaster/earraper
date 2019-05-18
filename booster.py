from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_mp3("snd.mp3")

sndloud = sound + 70

sndboosted = sndloud.low_pass_filter(2000)

play(sndboosted)

sndboosted.export("sndboosted.mp3", format='mp3')

