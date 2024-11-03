
from pwn import xor
string=bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
flag="myXORkey"
print(xor(string,flag))
'''
PIO OLOKLIROMENI TOU PAREA:D00Movenok
from pwn import xor
enc = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
key = xor(enc[:7], 'crypto{') + xor(enc[-1], '}') # we know first 7 bytes and the last 1
# the first part is 'myXORke' and the last is 'y'
print(xor(enc, key))
'''
