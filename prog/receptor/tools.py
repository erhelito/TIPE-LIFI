def display_raw(photo, base):
    return photo.read_u16(), base.read_u16(), photo.read_u16() - base.read_u16()

def binary(photo, base, treshold):
    return abs(photo.read_u16() - base.read_u16()) > treshold