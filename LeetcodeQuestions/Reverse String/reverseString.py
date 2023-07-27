from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

if __name__ == "__main__":
    solution = Solution()
    my_list = ["h", "e", "l", "l", "o"]
    solution.reverseString(my_list)
    print(my_list)
