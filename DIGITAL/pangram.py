# # Pangram is a sentence which contains all the alphabets starting from a-z
# def isPangram(s):
#     op = [0]*26
#     for i in range(26):
#         op[i] = False
    
#     for c in s.lower():
#         if not c == " ":
#             op[ord(c) -ord('a')]= True
    
#     for ch in op:
#         if ch == False:
#             return False
#         else:
#             return True



# if __name__ == "__main__":
#     s = "The Quick Brown Fox Jumps Over the lazy dog"
#     result = isPangram(s)
#     if result:
#         print(s + " is a Pangram")
#     else:
#         print(s + " is not a pangram")


def isPangram(s,k):
    op = [0]*26
    for i in range(26):
        op[i] = False
        
    for c in s.lower():
        if not c == " ":
            op[ord(c) -ord('a')]= True
            
    count = 0
    for i in op:
        if i == False:
            count+=1
    
    if count > k:
        return 0
    elif count <= k:
        return 1

n = int(input())
for i in range(n):
    s = input()
    k = int(input())
    print(isPangram(s,k))