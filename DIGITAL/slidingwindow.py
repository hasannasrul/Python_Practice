def slidingWindow(arr,n,k):
    curr_sum = 0
    max_sum = 0
    for i in range(k):
        curr_sum+=arr[i]
        
    for j in range(k,n):
        curr_sum+=arr[j] - arr[j-k]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum
        


arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
k = 4
print(slidingWindow(arr,n,k))