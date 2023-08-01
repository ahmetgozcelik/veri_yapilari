from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHashMap = {}

        for ix,num in enumerate(nums):
            difference = target - num
            if difference in myHashMap:
                return [myHashMap[difference], ix]
            myHashMap[num] = ix

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
