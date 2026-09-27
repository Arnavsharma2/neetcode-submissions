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
        def dfs(curr):
            if curr in visited:
                return visited[curr]
            
            visited[curr] = Node(curr.val)
            for neigh in curr.neighbors:
                dfs(neigh)
                visited[curr].neighbors.append(visited[neigh])
        
        dfs(node)
        return visited[node]
