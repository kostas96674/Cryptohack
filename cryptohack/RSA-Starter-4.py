def egcd(a, b):
    # Base Case
    if a == 0 :
        return b,0,1
    gcd,x1,y1 = egcd(b%a, a)

    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1

    return gcd,x,y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
p = 857504083339712752489993810777

q = 1029224947942998075080348647219

def Totient(p,q):
    return (p-1)*(q-1)
print(modinv(65537,Totient(p,q)))
