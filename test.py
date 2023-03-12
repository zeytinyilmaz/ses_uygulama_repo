from pydub import AudioSegment
from pydub.generators import Sine

do = 261.63
mi = 329.63

saniye1 = 1000
saniye2 = 2000



ses1 = Sine(do).to_audio_segment(duration=saniye1)
ses2 = Sine(mi).to_audio_segment(duration=saniye2)



birlestir = ses1 + ses2

Sine(mi).generate()

birlestir.export('/home/pentest/Masaüstü/sesdeneme.wav', format='wav', tags={'artist': 'project', 'album': 'project', 'comments': 'project'})

sound = AudioSegment.from_file("/home/pentest/Masaüstü/assets/notes/Gb7.wav", format="wav")
print(sound.frame_rate)

ses1 = Sine(sound.frame_rate).to_audio_segment(duration=saniye1)
ses1.export('/home/pentest/Masaüstü/sesdeneme.wav', format='wav', tags={'artist': 'project', 'album': 'project', 'comments': 'project'})
print('bitti')