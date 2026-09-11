class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = ""
        if len(s) == 0:
            return 0
        maxLen = 1
        setTrack = set(s[0])
        
        l = 0
        for r in range(1, len(s)):
            if s[r] not in setTrack:
                setTrack.add(s[r])
            else:
                l = r
                setTrack = set(s[l])
            maxLen = max(maxLen, r-l+1)

        return maxLen 