class Solution:
    def numDecodings(self, s: str) -> int:
        
        # 10 1 2
        # 10 12
        if s[0] == '0':
            return 0
        
        memo = {}

        def dfs(i):
            if i == len(s):
                return 1
            elif i > len(s):
                return 0
            if s[i] == '0':
                return 0
            
            if i in memo:
                return memo[i]



            if i + 1 < len(s) and int(s[i:i+2]) > 26:
                take = dfs(i + 1)
                memo[i] = take
                return take
            else:
                take = dfs(i + 1)
                skip = dfs(i + 2)
                memo[i] = take + skip
                return take + skip
            
        
        return dfs(0)
        
            