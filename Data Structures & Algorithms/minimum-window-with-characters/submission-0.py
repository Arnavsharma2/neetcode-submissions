class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = 0 
        need = len(t)
        needDict = {}
        for char in t:
            needDict[char] = needDict.get(char, 0) + 1
        minStr = s + 'i'

        l = 0
        for r in range(len(s)):
            if s[r] in needDict:
                if needDict[s[r]] > 0:
                    have += 1

            while have == need:
                if len(minStr) > r-l+1:
                    minStr = s[l:r+1]

                if s[l] in needDict:
                    if needDict[s[l]] > 0:
                        have -=1 
                l += 1             
        
        if minStr == s + 'i':
            return ''
        return minStr
                


