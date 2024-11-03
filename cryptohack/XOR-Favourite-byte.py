from pwn import xor
string=bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d").decode()
decoding="100000000000000000000000000000000"
def rotate(input,d):
   Rfirst = input[ : len(input)-d]
   Rsecond = input[len(input)-d : ]
   return Rsecond + Rfirst
for i in range(len(decoding)):
    print(xor(string,decoding).decode())
    decoding=rotate(decoding,1)
