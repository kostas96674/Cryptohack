

from Crypto.Util.number import *
string="0x696d70726573736976655f626c76645f636f6d706c69616e74"

print(int(string,16))#Convert the string to an integer and the base of string is 16

"""
print(long_to_bytes(0x6c617469747564655f737563636565645f686176696e67))
print(type(str(long_to_bytes(0x6c617469747564655f737563636565645f686176696e67)).replace("'","").replace("b","")))
string =long_to_bytes(0x6c617469747564655f737563636565645f686176696e67)
print(string)
"""
print(long_to_bytes(int(string,0)))#Convert the string to an integer by its prefix
