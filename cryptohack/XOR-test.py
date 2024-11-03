

string="label"
integer="13"
part1=(' '.join(format(ord(x), 'b') for x in string))
XOR=[(ord(a) ^ 13) for a in string]
print(XOR)
str=""
for i in XOR:
    str=str+chr(i)
print(str)
