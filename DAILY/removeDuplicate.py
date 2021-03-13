# Time complexity O(N)
def duplicate(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] == 0:
            return nums[i]
            

nums = [3,1,3,4,4,2]
print(duplicate(nums))