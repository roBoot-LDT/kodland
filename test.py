
def twoSum(nums, target):
    seen = {}
    for id, number in enumerate(nums):
        if target - number in seen:
            return [id, seen[target-number]]
        else:
            seen[number] = id
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
print(twoSum([3,2,3], 6))
