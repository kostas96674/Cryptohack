
from pwn import xor
string=bytes.fromhex("d7cfefdee6e6fecdf4cbed9cadd5c6c1ea8eeccbfac3bfdaf08ef7cff1caf3cbbfdaf7c7ec80bfe9f0c1fb8ef3dbfcc5bfc1f18eebc6fa8eeadefcc1f2c7f1c9bfcdf7cff3c2fac0f8cbecd3")
byte=""
for c in range(0,255):
    for i in range(0,255):
        byte=chr(c)+chr(i)
        print(xor(string,byte))
    byte=""
