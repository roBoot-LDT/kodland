
def twoSum(nums, target):
    if len(nums) == 2:
         return [0, 1]
    for first in nums:
        if first >= target:
            continue
        else:
            answer = [nums.index(first)]
            for second in nums:
                if second >= target or nums.index(first) == nums.index(second):
                        continue
                else:
                     if second + first == target:
                          answer.append(nums.index(second))
                          return answer
print(twoSum([2, 7, 11, 15, 16, 17], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
