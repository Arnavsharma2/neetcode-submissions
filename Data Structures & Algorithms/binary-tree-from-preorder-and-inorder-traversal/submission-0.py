# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder = node left right
        # inorder = left node right
        self.inOrderDict = {}
        for i in range(len(inorder)):
            self.inOrderDict[inorder[i]] = i
        self.count = 0
        return self.dfs(0, len(inorder) - 1)
        
        
    
    def dfs(self, left, right):
        if left > right:
            return None

        root = TreeNode(preorder[self.count])
        self.count += 1

        index = self.inOrderDict[root.val]

        root.left = self.dfs(left, index - 1)
        root.right = self.dfs(index+1, right)

        return root
        
        
            
        

