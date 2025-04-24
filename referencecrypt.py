import random

def encrypt(text):
    #keygeneration
    padding = "abcdefghijklmnopqrstuvwxylzäöü 1234567890,.-;:_!?=ABCDEFGHIJKLMNOPQRSTUVWXYZÖÄÜ+#-"
    print(f"len of padding {len(padding)}")
    msgarray = []
    keystring = ""
    key = list(padding)
    #ranomize key
    random.shuffle(key)
    reference = {}
    i=0
    for a in key:
        try:
            reference[a]
        except:
            reference[a] = i
            i+=1


    #text
    for char in text:
        msgarray.append(str(reference[char]))
    msg = '.'.join(msgarray)
    
    for k in reference:
        keystring+=k
    return msg,keystring

def decrypt(text,key):
    msg = ""
    for i in text.split('.'):
        msg += key[int(i)]
    return msg

# EXAMPLE MANUEL ENCODING
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!.-:"
text = "7.4.11.11.14.26"
print(decrypt(text,key))

# EXAMPLE AUTO generation
text,key = encrypt("This is a hidden message encoded by referypt")
print(decrypt(text,key))
