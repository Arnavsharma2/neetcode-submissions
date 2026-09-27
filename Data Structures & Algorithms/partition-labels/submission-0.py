class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        totalFreq = {}
        partFreq = {}
        res = []
        for char in s:
            totalFreq[char] = totalFreq.get(char, 0) + 1
        
        l = 0 
        for r in range(len(s)):
            curr = s[r]
            partFreq[curr] = partFreq.get(curr, 0) + 1

            passs = True
            for key, freq in partFreq.items():
                if totalFreq[key] != freq:
                    passs = False
            if passs:
                res.append(r-l+1)
                l = r + 1
        
        return res
        


        
