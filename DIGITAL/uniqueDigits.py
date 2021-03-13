#Given a number N, the task is to count the number of unique digits in the given number.
def findUnique(n):
    counter = dict()

    #storing every integer in the dictionary and counting there occurence
    while(n!=0):
        rem = n%10
        if rem in counter.keys():
            counter[rem] += 1
        else:
            counter[rem] = 1
        n = n//10
    
    # declaring a result counter, and then looping through dict to find the key-value pairs having value = 1
    result = 0
    for key in counter:
        if counter[key] == 1:
            result+=1
    return result


if __name__ == "__main__":
    n = int(input("Enter Number: "))
    print(findUnique(n))