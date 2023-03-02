import time
import mido

mid = mido.MidiFile('src/midi_files/MIDI_sample.mid')
#mid = mido.MidiFile('src/midi_files/Am_I_Blue_AB.mid')

print('Before:')

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    # for msg in track:
    #     print(msg)

# for messages in mid.tracks[1]:
#     print(messages)

# print(mid.tracks[1])

print('After:')

track = mido.MidiTrack()
mid.tracks.append(track)
track.append(mido.Message('program_change', program=12, time=50))
track.append(mido.Message('note_on', note=64, velocity=64, time=32))
track.append(mido.Message('note_off', note=64, velocity=127, time=32))
mid.save('src/midi_files/new_song.mid')


mid = mido.MidiFile('src/midi_files/new_song.mid')

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)

print(len(mid.tracks))