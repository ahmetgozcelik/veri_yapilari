from typing import List
from inspect import stack
from xml.etree.ElementPath import ops


class Solution:
    def calPoints(self, ops: List[stack]) -> int:
        ops = ["5","2","C","D","+"]
        stack = []
        for i in ops:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(stack[-1] *2)
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)
    
sol = Solution()
result = sol.calPoints(ops)
print(result)