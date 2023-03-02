import time
import mido

mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

track.append(mido.Message('program_change', program=12, time=0))
track.append(mido.Message('note_on', note=64, velocity=1, time=32))
track.append(mido.Message('note_off', note=64, velocity=127, time=320))
track.append(mido.Message('note_on', note=64, velocity=1, time=32))
track.append(mido.Message('note_off', note=64, velocity=127, time=320))

mid.save('src/midi_files/new_song.mid')


song = mido.MidiFile('src/midi_files/new_song.mid')

for i, track in enumerate(song.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)
