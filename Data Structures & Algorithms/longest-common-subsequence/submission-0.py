class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # “What’s the longest common subsequence using the remaining strings starting at indices i and j?”


        memo = {}
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + dfs(i +1, j + 1)
            
            if (i, j) in memo:
                return memo[i, j]
            
            explore = max(dfs(i, j + 1), dfs(i + 1, j))

            memo[(i, j)] = explore
            
            return explore


        return dfs(0, 0)

