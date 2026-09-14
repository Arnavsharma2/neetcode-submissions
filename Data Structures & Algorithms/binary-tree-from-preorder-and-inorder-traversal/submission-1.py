# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.indices = {}
        for i in range(len(inorder)):
            self.indices[inorder[i]] = i
        
        self.preIndex = 0
        return self.dfs(0, len(inorder)-1)
    
    def dfs(self, left, right):
        if left > right:
            return None
        
        root = TreeNode(preorder[self.preIndex])
        self.preIndex += 1

        index = self.indices[root.val]

        root.left = self.dfs(left, index - 1)
        root.right = self.dfs(index + 1, right)
        
        return root



