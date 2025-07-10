from machine import Pin, PWM, ADC # type: ignore
from math import cos, pi
from time import sleep

def format_bis(entier, nb_bits):
    """
    Convertit un entier en binaire sur un nombre fixe de bits.

    Args:
        entier (int): L'entier à convertir.
        nb_bits (int): Le nombre de bits pour la représentation binaire.

    Returns:
        str: La représentation binaire de l'entier sur le nombre de bits spécifié.
    """
    # Convertit l'entier en binaire
    binaire = ""
    while entier > 0:
        binaire = str(entier % 2) + binaire
        entier //= 2

    # Ajoute des zéros de remplissage si nécessaire
    while len(binaire) < nb_bits:
        binaire = "0" + binaire

    # Tronque la chaîne si elle est trop longue
    if len(binaire) > nb_bits:
        binaire = binaire[-nb_bits:]

    return binaire

led = Pin('LED', Pin.OUT)
laser = Pin(16, Pin.OUT)

# Alphabet personnalisé codé sur 32 caractères (chacun pouvant ainsi être codé sur 5 bits)
alphabet = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,
            'm':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,
            'x':24,'y':25,'z':26,' ':27,',':28,'.':29,'!':30,'?':31,"'":32}

# Inversion du dictionnaire pour obtenir une correspondance valeur -> lettre
tebahpla = {i: j for j, i in alphabet.items()}

def text_to_binary(message): #Entrée : str
    # Stocker le résultat
    binary_message = ""
    # Parcourir chaque caractère
    for c in message:
        if c in alphabet:
            # On attribue une valeur au cractère
            value = alphabet[c]
            # Convertir la valeur en binaire sur 5 bits
            binary_c = format_bis(value, 5)
            binary_message += binary_c
        else:
            print("Caractère '{c}' non supporté dans l'alphabet personnalisé.")
    return binary_message

def hamming_encode(str):
    reverse_str=str[::-1]
    n=len(str)
    k = 0
    while (2 ** k) < (n + k + 1): #Calcul du nombre k de bits de contrôle
        k += 1
    result = [0 for u in range (n+k)]
    i = 0
    for x in range(1,n+k+1): #Ajoute les bits d'informations aux bons emplacements
        if x & (x-1) != 0: #Vérifie si x n'est pas une puissance de 2, & est l'opérateur ET logique qui compare en binaire x et x-1.
            #L'idée avec x et x-1 est que si x est une puissance de 2, son binaire ne possède qu'un 1, x-1 inverse alors tous les bits.
            #Donc aucun des bits ne sera commun à x et x-1 donc "l'indicatrice" & ne s'allume jamais et on a 0.
            result[x-1]=reverse_str[i]
            i+=1
    bits_1=[]
    bin_bits_1=[]
    for x in range(n+k):
        if result[x] == '1':
            bits_1.append(x+1) #stock la position de tous les bits valant 1
    for x in bits_1:
        bin_bits_1.append(format_bis(x,k))
    parity=[0 for i in range(k)]
    for x in bin_bits_1:
        for i in range(len(x)):
            parity[i]+=int(x[::-1][i]) #Calcule la parité de chaque bit de contrôle
    for u in range(len(parity)):
        if parity[u]%2==1:
            result[(2**u)-1]='1' #Ajuste la valeur du bit de contrôle selon sa parité
    final=''
    for y in result[::-1]:
        final+=y
    return(final)

def emission(binary,f):
    binary2="1"+str(binary)+"1"
    for x in binary2:
        if x == "1":
            laser.high()
            sleep(1/f)
            laser.low()
        else:
            sleep(1/f)

#emission(101010101111110101010101010101010111,5)
#dire bonjour : emission(00010011110111001010011111010110010,5)

def text_to_light(message,f):
    return(emission(text_to_binary(message),f))

def text_to_light_hamming(message,f):
    return(emission(hamming_encode(text_to_binary(message)),f))