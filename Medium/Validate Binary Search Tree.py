# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node,low=float('-inf'), high=float('inf')):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            is_left= validate(node.left,low,node.val)
            is_right= validate(node.right, node.val,high)
            return is_left and is_right 
        return validate(root)