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


            if i + 1 < len(s) and int(s[i:i+2]) > 26:
                return dfs(i + 1)
            else:
                return dfs(i + 1) + dfs(i + 2)
        
        return dfs(0)
        
            