class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        maxLen =0
        mostCom={}
        for r in range(len(s)):
            mostCom[s[r]] = mostCom.get(s[r], 0) + 1
            com = max(mostCom.values())
            while r-l-com+1 > k:
                mostCom[s[l]] = mostCom.get(s[l], 0)-1
                l+=1
                com = max(mostCom.values())
            maxLen = max(r-l+1, maxLen)
        return maxLen





            