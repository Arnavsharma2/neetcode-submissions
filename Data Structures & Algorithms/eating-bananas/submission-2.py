class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = float('inf')
        while l <= r:
            m = (r-l)//2 + l

            hours = 0
            for pile in piles:
                if pile%m ==0:
                    hours += pile//m
                else:
                    hours += pile//m + 1
                
            if hours <= h:
                res = min(m, res)
                r = m - 1
            else:
                l = m + 1
            
        return res