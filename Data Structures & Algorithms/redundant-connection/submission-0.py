class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        adj = defaultdict(list)


        def dfs(node, target):
            if node == target:
                return True
            
            for n in adj[node]:
                if n not in visited:
                    visited.add(n)
                    if dfs(n, target):
                        return True
            
            return False

        for edge in edges:
            visited = set()
            if dfs(edge[0], edge[1]):
                return [edge[0], edge[1]]

            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        