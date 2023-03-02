# python file for conversions between different types of data

# converts an ascii string into a hex string
def message_to_hex(message):
    hex_message = message.encode('ascii').hex()
    return hex_message

# converts a hex string into an ascii string
def hex_to_message(hex_message):
    return bytearray().fromhex(hex_message).decode()