list=[105, 110, 115, 116, 114, 117, 99, 116, 105, 111, 110, 97, 108, 95, 101, 109, 112, 108, 111, 121, 101, 114, 115, 95, 97, 115, 104]

for i in list:
    print(chr(i), end="")

        if received["type"] == "base64":
            "decoded": base64.b64decode(received["encoded"])+""
        elif ereceived["type"] == "hex":
            "decoded": bytes.fromhex(received["encoded"])+""
        elif received["type"] == "rot13":
            "decoded": codecs.decode(received["encoded"], 'rot_13')+""
        elif received["type"] == "bigint":
            "decoded": long_to_bytes(received["encoded"])+""
        elif received["type"] == "utf-8":
            rr=""
            "decoded": for i in received["encoded"]: rr+=chr(i)
    if received["type"] == "base64":
        "decoded": base64.b64decode(received["encoded"])+""
        elif encoding == "hex":
            "decoded": bytes.fromhex(received["encoded"])+""
        elif encoding == "rot13":
            "decoded": codecs.decode(received["encoded"], 'rot_13')+""
        elif encoding == "bigint":
            "decoded": long_to_bytes(received["encoded"])+""
        elif encoding == "utf-8":
            rr=""
            "decoded": for i in received["encoded"]: rr+=chr(i)            
