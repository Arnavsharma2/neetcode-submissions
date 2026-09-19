class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        def dfs(word):
            if not word:
                return True
            

            for key in wordDict:
                if word[:len(key)] == key:
                    trimmed = word[len(key):]
                    if trimmed in memo:
                        return memo[trimmed]
                    elif dfs(trimmed):
                        memo[trimmed] = True
                        return True
                    else:
                        memo[trimmed] = False

            
            return False
        
        return dfs(s)
                

                