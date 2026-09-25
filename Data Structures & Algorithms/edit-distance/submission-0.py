class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    
        
        def dfs(i, j):
            if j >= len(word2):
                return len(word1) - i
            if i >= len(word1):
                return 1 + dfs(i+1, j+1)

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            
            insert = dfs(i+1, j+1)
            delete = dfs(i + 1, j)
            replace = dfs(i, j + 1)

            return 1 + min(insert, delete, replace)

        return dfs(0, 0)