
'''
from Crypto.PublicKey import RSA
with open("C:/Users/kosta/Desktop/cryptohack/key.der","rb") as f:
    content = f.read()
key=RSA.importKey(content)
print(key.n)
'''
from Crypto.PublicKey import RSA

f = open("C:/Users/kosta/Desktop/cryptohack/key.der", "rb")
key = RSA.importKey(f.read())
print("n =", key.n)
