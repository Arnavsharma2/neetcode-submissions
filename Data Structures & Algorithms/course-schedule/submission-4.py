class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for key, val in prerequisites:
            adj[key].append(val)

        safe = set()
        visited = set()
        def dfs(i):
            if i not in adj:
                return False
            if i in visited:
                return True
            if i in safe:
                return False
            
            for j in adj[i]:
                visited.add(i)
                if dfs(j):
                    return True
                visited.remove(i)

            safe.add(i)

        for i in range(numCourses):
            if dfs(i):
                return False
        
        return True
        
