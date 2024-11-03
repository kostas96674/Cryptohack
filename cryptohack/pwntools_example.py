from pwn import * # pip install pwntools
import json
import codecs
from Crypto.Util.number import *
import base64
r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


received = json_recv()

print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])

for i in range(1,101):
    _string = ""
    if received["type"] == "base64":
        _string  = base64.b64decode(received["encoded"]).decode('utf-8')
    elif received["type"] == "hex":
        _string  = bytes.fromhex(received["encoded"]).decode('utf-8')
    elif received["type"] == "rot13":
        _string  = str(codecs.decode(received["encoded"], 'rot_13'))
    elif received["type"] == "bigint":
        _string  = long_to_bytes(int(received["encoded"],16)).decode('utf-8')
    elif received["type"] == "utf-8":
        for i in received["encoded"]: _string +=chr(i)

    to_send = {
         "decoded" : _string+""
         }
    json_send(to_send)
    received = json_recv()
    _string = ""
