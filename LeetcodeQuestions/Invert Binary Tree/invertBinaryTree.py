from typing import Optional, Self


class Solution:
    def invertTree(self, root: Optional[Self.TreeNode]) -> Optional[Self.TreeNode]:
        #exit condition
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left

        #recursion
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root