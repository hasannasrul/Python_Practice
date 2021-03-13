def GCD(a,b):
    while(b!=0):
        temp = a
        a = b
        b = temp%a

    return a

print(GCD(20,8))
print(GCD(20,80))