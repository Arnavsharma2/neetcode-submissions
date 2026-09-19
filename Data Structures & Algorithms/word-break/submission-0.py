class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        def dfs(word):
            if not word:
                return True
            

            for key in wordDict:
                if word[:len(key)] == key:
                    if dfs(word[len(key):]):
                        return True
            
            return False
        
        return dfs(s)
                

                