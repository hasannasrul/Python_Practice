import math

def isAutomorphic(inp):
    sqr = inp*inp
    while(inp!=0):
        if(math.remainder(inp,10) != math.remainder(sqr,10)):
            return False
        sqr = sqr//10
        inp = inp//10
    return True

inp = int(input())
result = isAutomorphic(inp)
if result:
    print("Correct Number")
else:
    print("Incorrect Number")