from os import urandom #required for true randomness

mode = input("Program mode (1: Encryption, 2: Decryption, 3: Help): ") #Ask for mode
if(mode == ""): mode = 3
else: mode = int(mode)

def enc(stg, key): #The encryption algorithm
    if isinstance(stg, str): return b"".join(chr(ord(x) ^ ord(y)) for x, y in zip(stg, key))
    else: return bytes([x ^ y for x, y in zip(stg, key)])

if(mode == 1): #Mode 1: Encryption
    txt = input("Text to encrypt: ") #Ask for plaintext content
    hrd = input("Hardness multiplier (1 by default, but 10 is the maximum): ") #The encryption hardness variable's setup
    if(hrd == "" or int(hrd) > 10): lgth = len(txt) #If the hardness variable is empty of more than 10 (it can be more than 10 but it will slow down the computer and it will be hard to transmit), then the default value will be used (that's just as long as the text itself)
    else: lgth = len(txt)*int(hrd) #If the value was correct then the text length will be multiplied by that value
    for c in txt: #For hungarian characters
        c = c.lower() #for a smaller if
        if(c=="ö" or c=="á" or c=="é" or c=="ó" or c=="ü" or c=="ű" or c=="ú" or c=="ő" or c=="í"): lgth = lgth+1 #i was too lazy to make an array use it for searching, so this'll do
    key = bytes(urandom(lgth)) #we need true randomness, converted to byte format
    enctxt = enc(txt.encode('utf8'), key) #Calls the encryption function and gives the return text to a variable (makes the unencrypted text into UTF-8 (hungarian characters, etc), and uses the randomized key for the encryption), this is already in byte format
    print('Encrypted text:', enctxt) #Prints the encrypted text
    print("Encryption key: ", key) #Prints the encryption key
    print('Decrypted checking text:', enc(enctxt, key).decode("utf8")) #Checks the encryption both ways
    if enc(enctxt, key).decode('utf8') == txt: print("Successful encryption") #If the check is successful
    else: print("Failed encryption") #And if it isn't
if(mode == 2): #Mode 2: Decryption
    enctxt = eval(input("Encrypted text:: ")) #Asks for the encrypted text (requires the b' prefix)
    key = eval(input("Decryption key: ")) #Asks for the decryption key
    print('Decrypted text:', enc(enctxt, key).decode("utf8")) #Uses the same function as the encryption
if(mode == 3): #Mod 3: Help
    print("-----------------------------------------------------------------------------------------------")
    print("                                          2021 Oliver                                          ")
    print("1. How it works:")
    print("There are two modes in the program: encryption and decryption")
    print("These can be accessed from the main interface by entering the number combination specified.")
    print("The program can be exited by simply using the Ctrl+C key combination")
    print("The program only runs under Python 3, but could be easily backported to Python 2")
    print("How to run it: python3 XOR.py")
    print("")
    print("-----------------------------------------------------------------------------------------------")
