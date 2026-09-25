class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        visited = {}

        def dfs(i):
            if i >= len(cost):
                return 0
            elif i in visited:
                return visited[i]
            
            step1 = cost[i] + dfs(i + 1)
            step2 = cost[i] + dfs(i + 2)

            visited[i] = min(step1, step2)

            return min(step1, step2)
            
        return min(dfs(0), dfs(1))

        