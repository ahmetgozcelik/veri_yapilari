from typing import Optional, Self


class Solution:

    answer = -float("inf")

    def maxPathSum(self, root: Optional[Self.TreeNode]) -> int:
        self.dfs(root)
        return self.answer
        
    def dfs(self, node):
        if node is None:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        left = max(left, 0)
        right = max(right, 0)

        self.answer = max(self.answer, node.val+left+right)

        return node.val + max(left, right)