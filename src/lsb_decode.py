import mido

from utils import string_to_binary, binary_to_string

# create a MidiFile object
midi = mido.MidiFile('src/midi_files/new.mid')

# a list of the tracks in the midi file
tracks = midi.tracks

# track is track 1 in the tracks list
track = tracks[1]

# create an empty string for storing one long bit string
binary_string = ''

# for i in length of the track
for i in range(len(track)):
    # if the message type is note_on
    if (track[i].type == 'note_on'):
        # set bit to the velocity of the note_on message modulo 2 (either 0 or 1)
        bit = track[i].velocity % 2
        # append the bit to the end of the bit string
        binary_string += str(bit)

# create an empty list for holding the 8-bit strings
eight_bit_strings = []

# cut the one long bit string into 8-bit chunks and append them to the list
for i in range(0, len(binary_string), 8):
    eight_bit_strings.append(binary_string[i:i+8])

# assign to message the string resulting from converting the 8-bit strings to characters
message = binary_to_string(eight_bit_strings)

# print the message
print(message)