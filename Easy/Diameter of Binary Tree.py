# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiameter=0

        def count(node):
            if not node:
                return 0
            
            left= count(node.left)
            right= count(node.right)

            self.maxdiameter= max(self.maxdiameter, left+right)

            return 1 + max(left, right)

        count(root)
        return self.maxdiameter