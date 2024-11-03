from Crypto.PublicKey import RSA

f = open("C:/Users/kosta/Desktop/cryptohack/bruce_rsa_.pub", "rb")
key = RSA.importKey(f.read())
print("n =", key.n)
