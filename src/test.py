import time
import mido

midi = mido.MidiFile('src/midi_files/castles.mid')

# a list of the tracks in the midi file
tracks = midi.tracks

longest = 0

for i in range(len(tracks)):
    if len(tracks[i]) > longest:
        longest = i

print(len(tracks[longest]))

