class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            while stk and stk[-1][0] < temperatures[i]:
                temp, index = stk.pop()
                res[index] = i-index

            stk.append((temperatures[i], i))
            
        return res

