import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            distanceToOrigin = (x**2) + (y**2)
            minHeap.append([distanceToOrigin, x, y])

        heapq.heapify(minHeap)
        result = []

        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            k -= 1
        
        return result
    
sol = Solution()

print(sol.kClosest([[1,3],[-2,2]], 1))