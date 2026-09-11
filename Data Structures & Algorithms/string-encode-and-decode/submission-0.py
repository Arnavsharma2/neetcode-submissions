class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for word in strs:
            res += str(len(word))+'.'+word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = 0
        while l < len(s):
            num = ''
            while s[l] != '.':
                num += s[l]
                l+=1
            num = int(num)
            res.append(s[l+1:l+num+1])
            l += num + 1
        return res
            

