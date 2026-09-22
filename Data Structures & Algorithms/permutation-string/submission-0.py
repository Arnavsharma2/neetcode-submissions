class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = {}
        for char in s1:
            dict1[char] = dict1.get(char, 0) + 1
        
        dict2 = {}
        l = 0
        for r in range(len(s2)):
            if r < len(s1)-1:
                dict2[s2[r]] = dict2.get(s2[r], 0) + 1
                continue
            dict2[s2[r]] = dict2.get(s2[r], 0) + 1

            if dict1 == dict2:
                return True

            dict2[s2[l]] -= 1
            if dict2[s2[l]] == 0:
                del dict2[s2[l]]
            
            l += 1
        return False
            

