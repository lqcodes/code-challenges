def removeDuplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j+=1
            nums[j] = nums[i]
    return j+1


# Remove Duplicates from Sorted Array
# Expected 2
arr = [1,1,2]

result = removeDuplicates(arr)
print(result)