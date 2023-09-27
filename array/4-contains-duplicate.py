import time

# More slow way
# def containsDuplicate(nums):
#     rng = len(nums)
#     for i in range(0, rng):
#         for j in range(0, rng):
#             if i != j:
#                 if nums[i] == nums[j]:
#                     return True
#     return False

def containsDuplicate(nums):
    rng = len(nums)
    nums.sort()
    for i in range(1, rng):
        if nums[i] == nums[i-1]:
            return True
    return False

# Contains Duplicate
# Expected result True

arr = [1,2,3,1]

start_time = time.perf_counter()

response = containsDuplicate(arr)
print(response)

end_time = time.perf_counter()
print(f'Time to process: {end_time - start_time}')
