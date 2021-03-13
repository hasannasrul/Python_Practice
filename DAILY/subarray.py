# without altering array find the subset of array which equals to target sum
def subArray(a,target,n):
    for i in range(n):
        current_sum = a[i]
        for j in range(i+1,n):
            if current_sum == target:
                print(i,j-1)                #starting and ending index of subarray
                return True
            
            if current_sum > target:
                break

            current_sum += a[j]
    return False


################################ To Check if Target is present in the array  #######################

# def subArray(a,target,n):
#     a.sort()
#     i = 0
#     j = n-1
#     while(i!=j):
#         summation = a[i] + a[j]
#         if summation == target:
#             return True
        
#         if summation < target:
#             i+=1
        
#         elif summation > target:
#             j-=1
#     return False

####################################    Driver Code     #########################################
if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]  #[2,4,5,8,9,10,15,23]
    n = len(arr) 
    sum = 23
    
    print(subArray(arr, sum, n))


