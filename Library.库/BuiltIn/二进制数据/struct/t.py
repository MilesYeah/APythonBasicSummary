
def unpack6bitascii(inputdata):
    # This is a text encoding scheme that seems unique
    # to IPMI FRU.  It seems to be relatively rare in practice
    result = ''
    while len(inputdata) > 0:
        
        currchunk = inputdata[:3]
        del inputdata[:3]
        currchar = currchunk[0] & 0b111111
        result += chr(0x20 + currchar)

        currchar = (currchunk[0] & 0b11000000) >> 6
        currchar |= (currchunk[1] & 0b1111) << 2
        result += chr(0x20 + currchar)

        currchar = (currchunk[1] & 0b11110000) >> 4
        currchar |= (currchunk[2] & 0b11) << 4
        result += chr(0x20 + currchar)

        currchar = (currchunk[2] & 0b11111100) >> 2
        result += chr(0x20 + currchar)
    return result

