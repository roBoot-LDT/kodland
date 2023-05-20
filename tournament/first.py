############################################################
#               Задача №1
# Дан список из чисел nums, вернуть True, если в списке есть 
# повторяющиеся числа и False иначе (то-есть все числа
# встречаются 1 раз)
# 
#               Примеры:
#   Input: nums = [1,2,3,1]
#   Output: true
#   
#   Input: nums = [1,2,3,4]
#   Output: false
#
#   Input: nums = [1,1,1,3,3,4,3,2,4,2]
#   Output: true
############################################################
import time
class Solution:
    def containsDuplicate(self, nums: list[int]):
        return






############################Проверка############################
st = time.time()
print(Solution.containsDuplicate(None, [1,2,3,1]))             # -> True
print(Solution.containsDuplicate(None, [1,2,3,4]))             # -> False
print(Solution.containsDuplicate(None, [1,1,1,3,3,4,3,2,4,2])) # -> True
et = time.time()
print(f"Время выполнения кода: {et-st} секунд")
