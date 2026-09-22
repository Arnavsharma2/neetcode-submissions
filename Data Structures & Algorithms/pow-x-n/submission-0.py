class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def recurse(m):
            if m == 0:
                return 1.0
            
            half = recurse(m//2)

            if m%2==0:
                return half*half
            return half*half*x
        
        res = recurse(abs(n))

        if n < 0:
            return 1/res
        
        return res