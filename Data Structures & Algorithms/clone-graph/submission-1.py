"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        if not node:
            return None

        def clone(node):
            if node in visited:
                return visited[node]
            copy = Node(node.val)
            visited[node] = copy

            for nei in node.neighbors:
                neiCopy = clone(nei)
                copy.neighbors.append(neiCopy)
            return copy
            
        
        return clone(node)
