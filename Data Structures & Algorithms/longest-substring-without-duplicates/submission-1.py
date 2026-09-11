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
                while s[r] in setTrack:
                    setTrack.remove(s[l])
                    l += 1
                setTrack.add(s[r])
            maxLen = max(maxLen, r-l+1)

        return maxLen 