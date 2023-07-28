from typing import Optional, Self


class Solution:
    def convertBST(self, root: Optional[Self.TreeNode]) -> Optional[Self.TreeNode]:

        sumOfValues = 0
        def traverse(node):
            if not node:
                return
            
            nonlocal sumOfValues

            if node.right:
                traverse(node.right)

            temp = node.val
            node.val += sumOfValues
            sumOfValues += temp 

            if node.left:
                traverse(node.left)

        traverse(root)
        return root