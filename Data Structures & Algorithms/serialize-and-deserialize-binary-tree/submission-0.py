# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        queue = deque()
        queue.append(root)
        size = 1
        serial = ''
        while queue:
            for _ in range(size):
                node = queue.popleft()
                if node:
                    serial += str(node.val) + ','
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    serial += 'X,'
            size = len(queue)
        return serial
                        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        queue = deque()
        if data == 'X,':
            return None

        arr = data.split(',')

        root = TreeNode(int(arr[0]))

        queue.append(root)
        levels = 1
        index = 1
        while queue:
            for _ in range(levels):
                node = queue.popleft()
                if node:
                    if arr[index] != 'X':
                        node.left = TreeNode(arr[index])
                    else:
                        node.left = None
                    queue.append(node.left)
                    index += 1
                    if arr[index] != 'X':
                        node.right = TreeNode(arr[index])
                    else:
                        node.right = None
                    queue.append(node.right)
                    index += 1
            levels = len(queue)
        

        return root



        






