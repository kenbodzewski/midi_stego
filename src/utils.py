# python file for conversions between different types of data

# function for taking in a string and converting it to a list of binary numbers
# each binary number will have exactly 8 digits, and represent an ASCII character
def string_to_binary(message):
    # empty list for storing the binary strings
    binary_strings = []

    # for every character in the message string
    for i in range(len(message)):
        # set char to the character of the string
        char = message[i]
        # convert the character into a decimal number using the built in ord() function
        dec = ord(char)
        # convert the decimal number into a binary number and remove the leading '0b'
        binary = bin(dec).replace('0b', '')

        # while the binary string is shorter than 8 bits, keep adding leading zeroes
        # this is because some character will be less than 8 bits but we need it 
        # to always be the same
        while (len(binary) < 8):
            binary = '0' + binary
        
        # append to the list the binary string
        binary_strings.append(binary)
    
    # return the list of binary strings
    return binary_strings


# converts a list of 8bit binary strings to the corresponding ASCII string
def binary_to_string(binary_strings):
    # empty string for storing the ASCII string/message
    message = ''

    # for every 8bit string in the list 'binary_strings'
    for i in range(len(binary_strings)):
        # set binary to the 8bit string in 'binary_strings'
        binary = binary_strings[i]
        # convert the binary string to a decimal number using the built in int() function
        dec = int(binary, 2)
        # convert the decimal number to its corresponding ASCII character using built in
        # chr() function
        character = chr(dec)
        # add the character to the end of the message string
        message += (character)
    
    # return the message string
    return message















# converts an ascii string into a hex string
def message_to_hex(message):
    hex_message = message.encode('ascii').hex()
    return hex_message

# converts a hex string into an ascii string
def hex_to_message(hex_message):
    return bytearray().fromhex(hex_message).decode()

# converts a hex number into a base 10 integer
def hex_to_int(hex):
    return int(hex, 16)

