## Repo for Ken's CY 5210 Audio Steganography, Semester Long Project for Digital Forensics

This repo contains two audio (midi) steganography programs:

1. The first is made up of encode.py and decode.py. These embed and reveal hidden text messages that are encoded into a midi file. They work quite simply by creating a new (empty) track in the midi file, then encoding text as decimal numbers into the note_on messages' 'note' attribute with a 'velocity' of 0. This makes a track full of midi note_on messages that contain note/pitch data but do not actually produce any sound. The decoder works by finding the track at the largest track index (this is where the encoded message track was added), and converting decimal numbers into their unicode counterparts, then printing it to the console.

2. The second pair of programs are lsb_encode.py and lsb_decode.py. These are a little bit more complicated. Rather than creating a new track and adding notes with no volume, they instead alter the data in an existing track in such a subtle way that it is undetectable (to my ears).<br>
**Here are the steps for LSB encoding the message into the midi file:**

    * The first step is to find the longest track in the midi file and count how many note_on messages there are in the track. Then you can calculate how long the hidden message can be without exceeding the space available in the track.

    * Create a message that you want to encode in the midi file. Append to the front of the message the number of characters in the message, this way the decoder knows how many characters to decode from the midi track.

    * One character at a time convert the string message into a list of 8-bit strings such that each 8-bit string represents one character.

    * Embed the message into the midi track using least significant bit encoding.
        * Iterate through the midi track and list of 8-bit strings at the same time, altering the least significant bit in each 'note_on' messages of the midi track, to match that of the bit in the bit string (adding or subtracting 1).
    
    * Save the modified midi file, and print the message that you are hiding to the command line.<br><br>

    **Here are the steps for decoding the LSB message an encoded midi file:**

    * Locate the longest track in the midi file, since this is where the message will be encoded. 

    * Decode just the first three characters in the message to determine the total length of the encoded message.
        * First get the three 8-bit strings
        * Convert them to their corresponding unicode

    * Loop through the track that was identified above, and for every 'note_on' message concatenate the least significant bit (string) to the end of a string for storing the whole bit string - this will be equal in length to 8 * the length of the message string. 

    * Convert the (super) long bit string into an array of 8-bit strings. 

    * Convert the array of 8-bit strings into the message - each 8-bit string converts to one unicode character.

    * Print the hidden message to the console.


