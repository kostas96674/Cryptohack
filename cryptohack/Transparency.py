from Crypto.PublicKey import RSA
import hashlib
f = open("C:/Users/kosta/Desktop/cryptohack/transparency.pem", "rb")
key = RSA.importKey(f.read())
der = key.publickey().exportKey("DER")
m = hashlib.sha256()
m.update(der)
print(m.hexdigest()) #it gives me the sha256 fingerprint, which acts as an ID for a certificate
