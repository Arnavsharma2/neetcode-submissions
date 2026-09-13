# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.dfs(root, float('-inf'), float('inf'))
    
    def dfs(self, root, lower, upper):
        if not root:
            return True

        if not lower < root.val < upper:
            return False
        
        return self.dfs(root.left, lower, root.val) and self.dfs(root.right, root.val, upper)



