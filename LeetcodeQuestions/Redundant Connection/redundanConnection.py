from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = []

        for i in range(len(edges) + 1):
            parents.append(i)

        ranks = [1] * (len(edges) + 1)

        def find(n):
            parent = parents[n]
            while parent != parents[parent]:
                #path compression
                parents[parent] = parents[parents[parent]]
                parent = parents[parent]
            return parent
        
        def union(n1, n2):
            parent1, parent2 = find(n1), find(n2)

            if parent1 == parent2:
                #connected
                return False
            
            if ranks[parent1] > ranks[parent2]:
                parents[parent2] = parent1
            else:
                parents[parent1] = parent2
                ranks[parent2] += ranks[parent1]
            return True
        
        for n1, n2 in edges:
            if not union(n1 ,n2):
                return [n1, n2]
            
sol = Solution()
print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))
print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))