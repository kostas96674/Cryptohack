from Crypto.PublicKey import RSA
with open('privacy_enhanced_mail.pem','r') as f:
    content = f.read()
key=RSA.importKey(content)

print(key.d)
