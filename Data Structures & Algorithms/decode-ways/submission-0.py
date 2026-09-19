class Solution:
    def numDecodings(self, s: str) -> int:
        
        # 10 1 2
        # 10 12
        if s[0] == '0':
            return 0

        def dfs(i):
            if i == len(s):
                return 1
            elif i > len(s):
                return 0
            if s[i] == '0':
                dfs(i + 1)
            
            take = dfs(i + 2)
            dont = dfs(i + 1)

            return take + dont
        
        return dfs(0)
        
            