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
        
        self.lower = [float('inf')]
        self.upper = [float('-inf')]
        
        return self.dfs(root) and self.isValidBST(root.left) and self.isValidBST(root.right)


    
    def dfs(self, root):
        if not root:
            return True

        if root.left and root.left.val >= root.val:
            return False

        if root.right and root.right.val <= root.val:
            return False
        
        self.lower[0] = min(self.lower[0], root.val)
        self.upper[0] = max(self.upper[0], root.val)
        
        return self.dfs(root.left) and self.dfs(root.right)



