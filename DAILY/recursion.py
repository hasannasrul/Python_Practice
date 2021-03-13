####################################################  factorial  ######################################################
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

# if __name__ == "__main__":
#     n = int(input("Enter Number : "))
#     print(factorial(n))

def extraLongFactorials(n):
    memo = {}
    if n in memo:
        return memo[n]
    elif n == 0:
        return 1
    else:
        x = extraLongFactorials(n-1) * n
        memo[n] = x
        return x

if __name__ == "__main__":
    n = int(input("Enter Number : "))
    print(extraLongFactorials(n))












####################################################  fibonacci  ######################################################


###############  best solution   ######################

# def fib_to(n):
#     fibs = [0, 1]
#     for i in range(2, n+1):
#         fibs.append(fibs[-1] + fibs[-2])
#     return fibs[n]

# print(fib_to(5))

###############  second best solution   ##################

# def fib(n, computed = {0: 0, 1: 1}):
#     if n not in computed:
#         computed[n] = fib(n-1, computed) + fib(n-2, computed)
#     return computed[n]


# print(fib(999))

#################################################  prime Number  ################################################