"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.visit = {}
        self.node = node
        if not node:
            return None
        return self.dfs(node)

    def dfs(self, node):
        if node in self.visit:
            return self.visit[node]
        copy = Node(node.val)
        self.visit[node] = copy

        for neighbor in node.neighbors:
            neighborCopy = self.dfs(neighbor)
            copy.neighbors.append(neighborCopy)

        return copy
            
