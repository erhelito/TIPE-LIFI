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

def hamming_decode(stri):
    reverse_str=list(stri[::-1])
    n=len(stri)
    k = 0
    while (2 ** k) < (n + 1): #Cherche le nombre de bits de contrôle
        k += 1
    result=[]
    bits_1=[]
    bin_bits_1=[]
    for x in range(n):
        if reverse_str[x] == '1':
            bits_1.append(x+1) #stock la position de tous les bits valant 1
    for x in bits_1:
        bin_bits_1.append(format_bis(x,k))
    parity=[0 for i in range(k)]
    for x in bin_bits_1:
        for i in range(len(x)):
            parity[i]+=int(x[::-1][i]) #Calcule la parité de chaque bit de contrôle
    ok=0 #Tant que ok=0, aucune erreur détectée
    bit_error = 0
    for u in range(len(parity)):
        if parity[u]%2==1:
            ok+=1
            bit_error+=2**u
            index_bit_error=bit_error-1
    if ok == 0:
        print("Aucune erreur détectée")
    else:
        print("Erreur détectée au bit",bit_error)
        reverse_str[index_bit_error] = '0' if reverse_str[index_bit_error] == '1' else '1'
    for u in range(n):
        if u+1 & u != 0:
            result.append(reverse_str[u])
    final=''
    for y in result[::-1]:
        final+=y
    return final