# import the mido library
import mido

# import my own tools from utils
from utils import string_to_binary, binary_to_string


###############################################################################
####################        PUT YOUR MESSAGE HERE        ######################
###############################################################################

message = 'How long of a message can I put in this midi?'

###############################################################################
###############################################################################

# file path to midi file
input_file = 'src/midi_files/MIDI_sample.mid'

# create a MidiFile object
midi = mido.MidiFile(input_file)

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


###############################################################################
##########       determine longest message that can be hidden      ############
###############################################################################
# track is the longest track in the tracks list
track = tracks[longest_track_index]

# create a variable for storing the number of note_on messages in track
total_note_on = 0

# for each note in the track
for note in track:
    # if the note's type is 'note_on then increment total_note_on
    if (note.type == 'note_on'):
        total_note_on += 1

# print the longest message that you can hide
# print(f'the longest message that you can hide is: {total_note_on // 8} characters')

# save to message_max, the maximum character length that the message can be
message_max =  total_note_on // 8


###############################################################################
#######     append the message length to the front of the string      #########
###############################################################################
# find the length of the message (and add three for the length 'message_length')
# and typecast it to a string
message_length = str(len(message) + 3)

# add leading zeroes to the message_length string until it is 3 characters long
while (len(message_length) < 3):
    message_length = '0' + message_length

# add the string message_length to the front of the message
message = message_length + message


###############################################################################
###############     make sure message fits in midi file      ##################
###############################################################################
# binary is a list of 8-bit strings, one 8-bit string per character in the string
binary = string_to_binary(message)

# save the length of the string to variable string_length
string_length = len(binary)

# check to make sure the message will fit in the midi file
# if it is too long then quit and give user message below
if (string_length > message_max):
    quit('MESSAGE IS TOO LONG:'
            f'\n\tMaximum character length is {message_max} characters'
            f'\n\tYour message was {len(binary)} characters long')


###############################################################################
###############     embed the message in the midi file       ##################
###############################################################################
# set x and y to 0
x = 0
y = 0

# for i in range length of the track
for i in range(len(track)):
    # if the message type is 'note_on' and x has not exceeded the length of the bitstring
    if (track[i].type == 'note_on' and x < len(binary)):
        # print(binary[x][y % 8])
        # bit is set to the element at [x][y % 8]
        bit = binary[x][y % 8]
        # if remainder of the velocity of the note_on does not match the bit from above
        if ((track[i].velocity % 2) != int(bit)):
            # make sure that the track velocity isnt 127, if it is you need to subtract
            # rather than add because 127 is the max value
            if(track[i].velocity == 127):
                track[i].velocity -= 1
            # else add one to the velocity of the note so that it now matches
            else:
                track[i].velocity += 1
        # x should be set to y integer division 8 so that it resets every 8 character
        x = y // 8
        # add one to y so that we move to the next character
        y += 1


###############################################################################
#####################     save the new midi file       ########################
###############################################################################
# string for holding the file path for the midi file you want to save
output = 'src/midi_files/new.mid'

# save the midi as a new file
midi.save(output)

print(f'The following message was hidden in {output}\n\t', message[3:])
