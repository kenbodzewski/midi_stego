# import the mido library
import mido

# import my own tools from utils
from utils import string_to_binary, binary_to_string

# create a MidiFile object
midi = mido.MidiFile('src/midi_files/new.mid')

# a list of the tracks in the midi file
tracks = midi.tracks


###############################################################################
##################       identify the longest track:       ####################
###############################################################################
# create empty list for storing the length of each track
track_lengths = []

# for each track in tracks, append the length to the track_lengths list
for i in range(len(tracks)):
    track_lengths.append(len(tracks[i]))

# identify the longest track and grab its index position
longest_track_index = track_lengths.index(max(track_lengths))

# track is the longest track in the tracks list
track = tracks[longest_track_index]


###############################################################################
###########      determine the length of the hidden message      ##############
###############################################################################
# create empty string for storing bit string of message length
message_length_binary = ''
# create x so that it can be incremented
x = 0

# while the length of the message_length_binary is less than 24 bits long
while (len(message_length_binary) < 24):
    # if the message is a note_on message
    if (track[x].type == 'note_on'):
        # save the least significant bit
        bit = track[x].velocity % 2
        # add the bit as a string to message_length_binary
        message_length_binary += str(bit)
    # increment x
    x += 1

# create empty list for storing the bit strings for the message length
# 3 strings of 8 bits
message_length = []

# cut the one long bit string into 8-bit chunks and append them to the list
for i in range(0, len(message_length_binary), 8):
    message_length.append(message_length_binary[i:i+8])

print(message_length)

num = int(binary_to_string(message_length))

print(num * 8)

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