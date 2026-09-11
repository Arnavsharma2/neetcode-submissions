class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashDict = {}
        for word in strs:
            temp = [0]*26
            for char in word:
                temp[ord(char) - ord('a')] += 1
            
            temp = tuple(temp)
            if not temp in hashDict:
                hashDict[temp] = len(res)
                res.append([word])
            else:
                res[hashDict[temp]].append(word)
        return res