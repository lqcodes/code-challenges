def rotate(nums, k):
    k = k % len(nums)
    if k < 0:
        k += len(nums)
        
    reserve(nums, 0, len(nums) - k - 1)
    reserve(nums, len(nums) - k, len(nums) - 1)
    reserve(nums, 0, len(nums) - 1)

    print(nums)
        
        
def reserve(nums, i, j):
    li = i
    ri = j
    
    while li < ri:
        temp = nums[li]
        nums[li] = nums[ri]
        nums[ri] = temp
        
        li += 1
        ri -= 1
            

# Rotate Array
# Expected result [5, 6, 7, 1, 2, 3, 4]

arr = [1,2,3,4,5,6,7]
k = 3

rotate(arr, k)