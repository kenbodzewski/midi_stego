import time
import mido

midi = mido.MidiFile('src/midi_files/castles.mid')

# a list of the tracks in the midi file
tracks = midi.tracks

track_lengths = []

for i in range(len(tracks)):
    track_lengths.append(len(tracks[i]))

print(track_lengths)

longest_track_index = track_lengths.index(max(track_lengths))

print(longest_track_index)

print(len(tracks[longest_track_index]))


