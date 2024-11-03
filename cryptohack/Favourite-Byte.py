
from pwn import xor
string=bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
for c in range(0,255):
    print(xor(string, c.to_bytes(1, 'little')))
