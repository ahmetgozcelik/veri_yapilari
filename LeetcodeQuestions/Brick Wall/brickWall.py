from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        myHashMap = {0:0}

        for row in wall:
           gapIndex = 0
           for brick in row[:-1]:
               gapIndex += brick
               myHashMap[gapIndex] = 1 + myHashMap.get(gapIndex, 0)

        maximumGapnumber = max(myHashMap.values())
        rowNumber = len(wall)
        return rowNumber - maximumGapnumber
    
sol = Solution()
print(sol.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))