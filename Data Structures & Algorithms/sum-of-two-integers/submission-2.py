class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 1 , 1 -> 10
        # 100, 111 -> 1011
        # 111, 111 -> 14 -> 1110

        carry = 0
        binA = bin(a)[2:]
        binB = bin(b)[2:]
        
        padd = ''
        while abs(len(binA) - len(binB)) != len(padd):
            padd += '0'

        if len(binA) < len(binB):
            binA = padd + binA
        else:
            binB = padd + binB

        i = 0
        res = ''
        for i in range(-1, -min(len(binA), len(binB))-1, -1):
            if binA[i] == '1' and binB[i] == '1':
                if carry == 1:
                    res += '1'
                else:
                    carry = 1
                    res += '0'
            else:
                if carry == 1:
                    res += '01'
                    carry = 0
                elif binA[i] == '1' or binB[i] == '1':
                    res += '1'
                else:
                    res += '0'
        
        if carry == 1:
            res += '1'
        res = res[::-1]
        return int(res,2)


