from ast import List


class Solution:    
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums)) #en iyi çözüm

#en kötü senaryo
# nums = [1,2,3,4,5,6,7,8,2]
# def solution():
#     hashSet = set()
#     for num in nums:
#         if num in hashSet:
#             return True
#         hashSet.add(num)
#     return False

# solution()

