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
                return 0
            if i-1 >= 0 and int(s[i]) > 6 and int(s[i-1]) >= 2:
                return 0
            
            return dfs(i + 1) + dfs(i + 2)
        
        return dfs(0)
        
            