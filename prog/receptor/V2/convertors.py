# personalized alphabet coded on 32 characters (each character can be coded on 5 bits)
alphabet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
            'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,
            'x':24,'y':25,'z':26,' ':27,',':28,'.':29,'!':30,'?':31,"'":32}

# inverting the dictionary to get a value -> letter
tebahpla = {i: j for j, i in alphabet.items()}

def list_to_str(list:list) -> str:
    output = ""
    for i in list :
        output += str(i)
    return output


def binary_to_text(binary_message, tebahpla:dict=tebahpla) -> str:
    """Convert a "01" string to a string of ASCII characters."""

    if type(binary_message) != str:
        binary_message = list_to_str(binary_message)

    message = ""

    # parse the binary string into groups of 5 bits
    for i in range(0, len(binary_message), 5):
        bit = binary_message[i:i+5]

        # convert the 5 bits to an integer, convert the integer to a character
        try :
            message += tebahpla[int(bit, 2)]

        # if wrong char
        except KeyError:
            message += "*"

    return message