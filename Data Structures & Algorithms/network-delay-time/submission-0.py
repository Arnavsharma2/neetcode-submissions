class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for ui, vi, ti in times:
            adj[ui].append((vi, ti))
        
        visited = {}
        def paths(curr, pathTime):
            if curr in visited and visited[curr] <= pathTime:
                return
            
            visited[curr] = pathTime
            best = float('inf')
            for tNode, time in adj[curr]:
                paths(tNode, pathTime + time)
            
        paths(k, 0)

        if len(visited) < n:
            return -1
        return max(visited.values())

