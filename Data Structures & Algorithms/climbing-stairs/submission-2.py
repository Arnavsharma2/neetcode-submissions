class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def paths(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 1
            elif n < 0:
                return 0
            


            one = self.climbStairs(n-1)   
            two = self.climbStairs(n-2)

            memo[n] = one + two


            return one + two

        return paths(n)