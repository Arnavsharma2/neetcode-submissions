class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        visited = {}


        def paths(i, total):
            if total == amount:
                return 1
            elif total > amount or i >= len(coins):
                return 0
            elif (i, total) in visited:
                return visited[(i, total)]
        
            skip = paths(i+1, total) 
            take = paths(i, total + coins[i])

            visited[(i, total)] = skip + take
            return skip + take
        
        return paths(0, 0)

            