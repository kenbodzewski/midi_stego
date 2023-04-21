import time
import mido

midi = mido.MidiFile('midi_files/MIDI_sample.mid')

# a list of the tracks in the midi file
tracks = midi.tracks

# print(tracks[1][0])
# print(tracks[1][1])
# print(tracks[1][2])
# print(tracks[1][3])
# print(tracks[1][4])
# print(tracks[1][5])
# print(tracks[1][-1])
# print(len(tracks))
# print(tracks[1][-3])
# print(tracks[1][-2])
# print(tracks[1][-1])


track_lengths = []

for i in range(len(tracks)):
    track_lengths.append(len(tracks[i]))
#print(track_lengths)

# print(track_lengths)

longest_track_index = track_lengths.index(max(track_lengths))

# print(longest_track_index)

# print(len(tracks[longest_track_index]))

# largest possible value that chr() function takes
character = chr(1114111)

# print(character)

# print(len(tracks))

# for track in tracks:
#     print(track[2])

print(mido.parse([0x00, 0xFF, 0x2F, 0x00]))
