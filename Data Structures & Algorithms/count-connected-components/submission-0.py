class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = set()
        res = 0

        def dfs(i):
            if i in visited:
                return
            
            visited.add(i)
            for neigh in adj[i]:
                dfs(neigh)
        
        for j in range(n):
            if j not in visited:
                dfs(j)
                res += 1
        
        return res



            


