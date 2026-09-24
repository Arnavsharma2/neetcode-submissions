# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = [True]

        def dfs(root):
            if not root:
                return 0
            
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)

            if abs(left-right) > 1:
                self.balance[0] = False

            return max(left, right)
            

        
        dfs(root)
        return self.balance[0]
