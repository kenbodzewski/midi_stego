import mido

from utils import string_to_binary, binary_to_string

# create a MidiFile object
midi = mido.MidiFile('src/midi_files/surfingalien.mid')

# a list of the tracks in the midi file
tracks = midi.tracks

# track is track 1 in the tracks list
track = tracks[1]

# binary is a list of 8-bit strings, one 8-bit string per character in the string
binary = string_to_binary('That message was too long, here is a shorter one.')

# set x and y to 0
x = 0
y = 0

# for i in range length of the track
for i in range(len(track)):
    # if the message type is 'note_on' and x has not exceeded the length of the string
    if (track[i].type == 'note_on' and x < len(binary)):
        # print(binary[x][y % 8])
        # bit is set to the element at [x][y % 8]
        bit = binary[x][y % 8]
        # if remainder of the velocity of the note_on does not match the bit from above
        if ((track[i].velocity % 2) != int(bit)):
            # then add one to the velocity of the note so that it now matches
            track[i].velocity += 1
        # x should be set to y integer division 8 so that it resets every 8 character
        x = y // 8
        # add one to y so that we move to the next character
        y += 1

# string for holding the file path for the midi file you want to save
output = 'src/midi_files/new.mid'

# save the midi as a new file
midi.save(output)
