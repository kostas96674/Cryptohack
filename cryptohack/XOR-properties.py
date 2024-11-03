KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_XOR_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_XOR_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

KEY1=bytes.fromhex(KEY1)
KEY2_XOR_KEY1=bytes.fromhex(KEY2_XOR_KEY1)
KEY2_XOR_KEY3=bytes.fromhex(KEY2_XOR_KEY3)
FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2=bytes.fromhex(FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2)
List_KEY1=[key1 for key1 in KEY1]
List_KEY2=[]
for i in range(len(KEY2_XOR_KEY1)):
    List_KEY2.append(KEY2_XOR_KEY1[i]^List_KEY1[i])
List_KEY3=[]
for i in range(len(KEY2_XOR_KEY3)):     
    List_KEY3.append(KEY2_XOR_KEY3[i]^List_KEY2[i])
Flag_list=[]
for i in range(len(FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2)):
    Flag_list.append(FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2[i]^List_KEY1[i]^List_KEY2[i]^List_KEY3[i])
Flag=""
for i in Flag_list:
    Flag=Flag+chr(i)
print(Flag)
