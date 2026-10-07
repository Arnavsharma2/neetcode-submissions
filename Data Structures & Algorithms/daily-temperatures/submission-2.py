class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i in range(len(temperatures)):
            stk.append((temperatures[i], i))
            stk.sort(reverse=True)

            while stk and stk[-1][0] < temperatures[i]:
                temp, index = stk.pop()
                res[index] = i-index
            
        return res

