# Nth smallest element from collection of array

def isNthSmallest(n,li,nth):
    li.sort()
    return li[nth-1]


n = int(input("Enter The number of Elements : "))
li = []
for i in range(0,n):
    inp = int(input())
    li.append(inp)

nth = int(input())
result = isNthSmallest(n,li,nth)
print(result)