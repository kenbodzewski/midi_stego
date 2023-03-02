import time
import mido

# import functions from local file for conversions
from text_conversion import message_to_hex, hex_to_int, hex_to_message

# bring in the midi file with a hidden message
mid = mido.MidiFile('src/midi_files/new_song.mid')

# create an empty array
int_list = []

# for each message in the last track of the midi file
for messages in mid.tracks[len(mid.tracks) - 1]:
    # print(messages)

    # if the message's type is note_on, then append the note value to int_list
    if messages.type == 'note_on':
        int_list.append(messages.note)

# print(int_list)

# create empty array for hex values
hex_list = []

# for each integer in int_list append to hex_list the integer as a hex value
for integer in int_list:
    # when converting to hex, '0x' is appended to the front of each value, omit this when appending
    hex_list.append(str(hex(integer))[2:])

# print(hex_list)

# create empty list for holding characters
char_list = []

# for each hex value in hex_list, append to char_list the converted hex value (will be a ascii char)
for hex in hex_list:
    char_list.append(hex_to_message(hex))

## store the message by joining the array
message = ''.join(char_list)

# print the hidden message 
print(f"Hidden message: {message}")