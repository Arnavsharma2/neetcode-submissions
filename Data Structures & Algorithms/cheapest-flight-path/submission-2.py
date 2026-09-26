class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for frm, to, price in flights:
            adj[frm].append((to, price))
        
        visited = {}
        
        def dfs(curr, moves):
            if moves > k+1:
                return float('inf')
            elif curr == dst:
                return 0
            elif (curr, moves) in visited:
                return visited[(curr, moves)]
            
            best = float('inf')
            for loc, cost in adj[curr]:
                newPrice = dfs(loc, moves + 1) + cost
                best = min(best, newPrice)

            visited[(curr, moves)] = best
            return best
        result = dfs(src, 0)
        return -1 if result == float('inf') else result

