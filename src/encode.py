# external imports
# import time
import mido

# import functions from local file for conversions
from utils import message_to_hex, hex_to_int, hex_to_message

# bring in the midi file that you want to encode with a message
mid = mido.MidiFile('midi_files/MIDI_sample.mid')

# create a midi track
track = mido.MidiTrack()
# append that midi track to the midi file that we read in on line 7
mid.tracks.append(track)

# this is the secret ascii message that will be embedded in the midi file
message = 'Hi Dr. Gary Cantrell'

# turn the message into an array of individual characters
message_list = [*message]

# create an empty array for storing the characters converted into hex values
message_list_hex = []

# for each char in message_list, append to message_list_hex the character's hex value
for i in message_list:
    message_list_hex.append(message_to_hex(i))

# empty array for storing ints converted from their hex values
message_list_int = []

# for each hex value in messge_list_hex, append to message_list_int the int value
for j in message_list_hex:
    message_list_int.append(hex_to_int(j))

# for each int in message_list_int, add a note to the track, that is a note_on message with the
# notes value equal to the int from message_list_int
for k in message_list_int:
    track.append(mido.Message('note_on', note= k, velocity=0, time=40))

output = 'midi_files/new_song.mid'
# save the midi as a new file
mid.save(output)

# print out
print(f"Encoded following message in {output}:\n\t{message}")