import base64
str_1="72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

str_1_encoded = bytes.fromhex(str_1)
print(str_1_encoded)
print(base64.b64decode(str_1_encoded))
