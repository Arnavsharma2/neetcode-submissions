class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        rep = bin(n)
        for i in range(len(rep)):
            if rep[i] == '1':
                res += 1
        return res