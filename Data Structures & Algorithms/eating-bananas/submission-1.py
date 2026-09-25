class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rMax = max(piles)
        rMin = 1
        res = rMax
        
        while rMin <= rMax:
            rMid = (rMax-rMin)//2 + rMin
            hours = 0
            for pile in piles:
                if pile % rMid > 0:
                    hours += pile//rMid + 1
                else:
                    hours += pile//rMid
            if hours <= h:
                res = min(res, rMid)
                rMax = rMid - 1
            else:
                rMin = rMid + 1
        
        return res

                




