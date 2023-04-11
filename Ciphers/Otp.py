

def encrypt(text, key):
    cipherText = ""
    cipher = []
    for i in range(len(key)):
        cipher.append(ord(text[i]) - ord('A') + ord(key[i]) - ord('A'))

    for i in range(len(key)):
        if cipher[i] > 25:
            cipher[i] = cipher[i] - 26

    for i in range(len(key)):
        x = cipher[i] + ord('A')
        cipherText += chr(x)

    return cipherText


def decrypt(s, key):
    plainText = ""
    plain = []
    for i in range(len(key)):
        plain.append(ord(s[i]) - ord('A') - (ord(key[i]) - ord('A')))

    for i in range(len(key)):
        if plain[i] < 25:
            plain[i] = plain[i] + 26

    for i in range(len(key)):
        x = plain[i] + ord('A')
        plainText += chr(x)

    return plainText


plaintext = "HELLO"
key = "MONEY"

enc = encrypt(plaintext.upper(), key.upper())
dec = decrypt(enc.upper(), key.upper())
print("Cipher text = "+enc)
print("Message = "+dec)
