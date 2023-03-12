from pydub import AudioSegment
from pydub.generators import Sine
from pydub.playback import play
import time

# nota adları ve frekansları
notes = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88
}

# timeline listesi
timeline = []

# nota kaydedici
def record_note(note_name):
    duration = 1 # nota süresi 1 saniye olarak ayarlandı
    freq = notes[note_name]
    sine_wave = Sine(freq).to_audio_segment(duration*1000)
    sine_wave.export(f"{note_name}.wav", format="wav")
    timeline.append((note_name, time.time()))

# gitar arayüzü
while True:
    note = input("Lütfen bir nota girin (C, D, E, F, G, A, B): ")
    if note in notes:
        play(Sine(notes[note]).to_audio_segment(500)) # nota çalınır
        record_note(note) # nota kaydedilir
    elif note == "exit":
        break

# timeline sıralanırfasasfsa
timeline.sort(key=lambda x: x[1])

# timeline üzerinde ses dosyası oluşturulur
start_time = timeline[0][1]
end_time = timeline[-1][1]
output = AudioSegment.silent(duration=0)
for note, time in timeline:
    audio = AudioSegment.from_wav(f"{note}.wav")
    output = output.overlay(audio, position=(time-start_time)*1000)
output.export("song.wav", format="wav")
