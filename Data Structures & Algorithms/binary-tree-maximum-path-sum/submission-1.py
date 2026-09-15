# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')
        self.dfs(root)
        if root.val > self.maxPath:
            return root.val
        return self.maxPath

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.maxPath = max(self.maxPath, root.val + left + right)

        return root.val + max(0, left, right)


    