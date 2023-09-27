def singleNumber(nums):
        nums.sort()
        max_index = len(nums) - 1
        print(nums)
        for i in range(0, len(nums)):
            print(nums[i])
            if len(nums) == 1:
                return nums[0]
            elif i == 0:
                 if nums[i] != nums[i + 1]:
                      return nums[i]
            elif i == max_index:
                 if nums[i] != nums[i - 1]:
                      return nums[i]
            elif nums[i] != nums[i + 1] and nums[i] != nums[i - 1]:
                    return nums[i]
            else:
                continue
    

# Single Number
# Expected result 1 = [2,2,1]
# Expected result 4 = [4,1,2,1,2]

arr = [4,1,2,1,2]

print(singleNumber(arr))