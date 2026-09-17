class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # no cycles, fully connected

        if n == 0:
            return True

        adj = defaultdict(list)

        for key, val in edges:
            adj[key].append(val)
            adj[val].append(key)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)

            for neigh in adj[i]:
                if neigh == prev:
                    continue
                if not dfs(neigh, i):
                    return False
            
            return True
        
        return dfs(0, -1) and len(visit) == n


            

        