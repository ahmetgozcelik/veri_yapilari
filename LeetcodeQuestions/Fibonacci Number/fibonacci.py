class Solution:
    def fib(self, n: int) -> int:

# My Solution

#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return self.fib(n-1) + self.fib(n-2)
            
# solution = Solution() 
# print(solution.fib(4))
# # 1-1-2-3


# :((((
        x , y = 0 , 1
        for i in range(n):
            x , y = y , x+y
        return x
    
solution = Solution()
print(solution.fib(10))