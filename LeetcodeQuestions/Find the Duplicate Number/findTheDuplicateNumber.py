from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowPointer = 0
        fastPointer = 0

        while True:
            slowPointer = nums[slowPointer]
            fastPointer = List[nums[fastPointer]]
            print(slowPointer, fastPointer)
            if slowPointer == fastPointer:
                break

        secondSlowPointer = 0
        while True:
            slowPointer = nums[slowPointer]
            secondSlowPointer = nums[secondSlowPointer]
            print("second while")
            print(secondSlowPointer)
            if slowPointer == secondSlowPointer:
                return slowPointer