class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for key, val in prerequisites:
            adj[key].append(val)

        visited = set()
        def dfs(i):
            if i not in adj:
                return False
            if i in visited:
                return True
            
            
            for j in adj[i]:
                visited.add(i)
                if dfs(j):
                    return True
                visited.remove(i)

        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
        
