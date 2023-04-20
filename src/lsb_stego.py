import mido

from utils import string_to_binary, binary_to_string

# create a MidiFile object
midi = mido.MidiFile('src/midi_files/MIDI_sample.mid')

# a list of the tracks in the midi file
tracks = midi.tracks

# bass is track 1 in the tracks list
bass = tracks[1]

# binary is a list of 8-bit strings, one 8-bit string per character in the string
binary = string_to_binary('Kentaro')

# set x and y to 0
x = 0
y = 0

# for i in range length of the bass track
for i in range(len(bass)):
    # if the message type is 'note_on' and x has not exceeded the length of the string
    if (bass[i].type == 'note_on' and x < len(binary)):
        # print(binary[x][y % 8])
        # bit is set to the element at [x][y % 8]
        bit = binary[x][y % 8]
        # if remainder of the velocity of the note_on does not match the bit from above
        if ((bass[i].velocity % 2) != int(bit)):
            # then add one to the velocity of the note so that it now matches
            bass[i].velocity += 1
        # x should be set to y integer division 8 so that it resets every 8 character
        x = y // 8
        # add one to y so that we move to the next character
        y += 1
          


binary_string = ''
for i in range(117):
    if (bass[i].type == 'note_on'):
        bit = bass[i].velocity % 2
        binary_string += str(bit)

eight_bit_strings = []

for i in range(0, len(binary_string), 8):
    eight_bit_strings.append(binary_string[i:i+8])

print(binary_to_string(eight_bit_strings))

output = 'src/midi_files/new.mid'
# save the midi as a new file
midi.save(output)
