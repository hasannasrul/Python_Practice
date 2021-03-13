#difference between sum of diagonals of square matrix

def sumDifference(M,size):
    #[0][0] + [1][1] + [2][2] - [0][2] + [1][1] + [2][0]
    left = 0
    right = 0

    for i in range(size):
        left+=M[i][i]
        right+=M[i][size-i-1]
    
    diff = right - left

    return diff
            


if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
            arr.append(list(map(int, input().rstrip().split())))
        
    print(sumDifference(arr,n))