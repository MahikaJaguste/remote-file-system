def encrypt(text, mode, e_d = 0): 
    
    if(mode == 2):
        result = "" 
        # shift
        if(e_d == 0): # encrpyt
            s = 2 
        else: # decrypt
            s = 24
        # traverse text 
        for i in range(len(text)): 
            char = text[i] 
            if not char.isalpha():
                result += char
                continue
            # Encrypt uppercase characters 
            if (char.isupper()): 
                result += chr((ord(char) + s-65) % 26 + 65) 
            # Encrypt lowercase characters 
            else: 
                result += chr((ord(char) + s - 97) % 26 + 97) 
        return result 

    elif(mode == 3):
        return ' '.join(word[::-1] for word in text.split(" "))

    else: # plaintext or invalid mode
        return text


 
###### Testing ######

# text = "ATTACKATONCE"
# print (encrypt(text, 'plaintext'))

# text = "ATTACKATONCE"
# print (encrypt(text, 'substitute'))

# text = "CVVCEMCVQPEG"
# print (encrypt(text, 'substitute', 1))

# text = "GeeksforGeeks is good to learn"
# print (encrypt(text, 'transpose'))

# text = "skeeGrofskeeG si doog ot nrael"
# print (encrypt(text, 'transpose'))
