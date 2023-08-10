from string import ascii_letters

# Encryption------------------------------------------
def encrypt (string, key):
    alpha = ascii_letters
    result =''
    for ch in string:
        if ch not in alpha:
            result += ch
        else:
            n_key = (alpha.index(ch) + key) % len(alpha)
            result += alpha[n_key]
    return result

print(encrypt('ِDivid', 4))     #ِHmzmh



# Decoding--------------------------------------------
def decrypt (string, key):
    key *= -1
    return encrypt(string, key)

print(decrypt('ِHmzmh', 4))     #Divid



# Brute_force--------------------------------------------
def brute_force(string):
    key = 1
    alpha = ascii_letters
    brute_force_data = {}
    result = ''
    while  key <= len(alpha) :
        result = decrypt(string, key)    #key=1
        brute_force_data[key] = result   #save input data
        result= ''
        key += 1
    return brute_force_data

print(brute_force('Hmzmh'))
