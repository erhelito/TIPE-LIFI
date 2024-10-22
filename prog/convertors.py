from PIL import Image

# personalized alphabet coded on 32 characters (each character can be coded on 5 bits)
alphabet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
            'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,
            'x':24,'y':25,'z':26,' ':27,',':28,'.':29,'!':30,'?':31,"'":32}

# inverting the dictionary to get a value -> letter
tebahpla = {i: j for j, i in alphabet.items()}

def binary_convertor_to_list(chain:str) -> list:
    """Convert a string of binary digits (0/1) to a boolean list."""
    output_list = []
    for char in chain:
        if char == '0':
            output_list.append(True)
        elif char == '1':
            output_list.append(False)
    return output_list

def binary_convertor_to_str(values:list) -> str:
    """Convert a boolean list to a string of binary digits (0/1)."""
    output_str = ""
    for value in values:
        if value:
            output_str += '1'
        else:
            output_str += '0'
    return output_str

def ascii_to_binary(ascii_message:str) -> list:
    """Convert a string of ASCII characters to a boolean list."""
    binary_message = ""
    
    for c in ascii_message:
        # get the ASCII value
        ascii_value = ord(c)
        # convert to binary, 8 bits
        binary_char = format(ascii_value, '08b')
        binary_message += binary_char

    return binary_convertor_to_list(binary_message)

def binary_to_ascii(binary_message:list) -> str:
    """Convert a boolean list to a string of ASCII characters."""
    ascii_message = ""
    binary_message = binary_convertor_to_str(binary_message)

    # parse the binary string into groups of 8 bits
    for i in range(0, len(binary_message), 8):
        bit = binary_message[i:i+8]
        
        # convert the 8 bits to an integer, convert the integer to an ASCII character
        ascii_char = chr(int(bit, 2))
        ascii_message += ascii_char

    return ascii_message

def text_to_binary(message:str, alphabet:dict=alphabet) -> list:
    """Convert a string of characters to a boolean list."""
    binary_message = ""
    
    try :
        for c in message:
                value = alphabet[c]

                # convert the value to binary, 5 bits
                binary_c = format(value, '05b')
                binary_message += binary_c

    except KeyError:
        print("Character not found in the alphabet")

    return binary_convertor_to_list(binary_message)

def binary_to_text(binary_message:list, tebahpla:dict=tebahpla) -> str:
    """Convert a boolean list to a string of ASCII characters."""
    message = ""
    binary_convertor_to_str(binary_message)

    # parse the binary string into groups of 5 bits
    for i in range(0, len(binary_message), 5):
        bit = binary_message[i:i+5]

        # convert the 5 bits to an integer, convert the integer to a character
        message += tebahpla[int(bit, 2)]

    return message

def image_to_binary_grayscale(image:str) -> list:
    """Convert a grayscale image to a boolean list.

    Args:
        image (str): Path to the image file r'path'."""
    img = Image.open(image)

    # convert image to greyscale
    img_grayscale = img.convert('L')  # 'L' for 256 levels of grey, 8 bits

    img_bin = ""

    # the 4 first bytes contain the width and height of the image
    width, height = img_grayscale.size

    img_bin+=format(width, '016b')
    img_bin+=format(height, '016b')

    for y in range(height):
        for x in range(width):
            pixel_value = img_grayscale.getpixel((x, y))
            # convert the value to binary, 8 bits
            pixel_value_bin = format(pixel_value, '08b')
            img_bin += pixel_value_bin

    return binary_convertor_to_list(img_bin)

def binary_to_image_grayscale(binary_image:list) -> Image:
    """Convert a boolean list to a grayscale image."""
    binary_str = binary_convertor_to_str(binary_image)


    output_list = []
    width = binary_str[0:16]
    height = binary_str[16:32]

    # split the binary string into blocks of 8 bits, convert each block to an integer
    for i in range(32, len(binary_str), 8):
        bit = binary_str[i:i+8]
        pixel_value = int(bit, 2)
        output_list.append(pixel_value)

    img = Image.new('L', (int(width, 2), int(height, 2)))  # 'L' for 256 levels of grey, 8 bits

    # add the pixels to the image
    img.putdata(output_list)
    img.show()
    img.save("output.png")
    return img