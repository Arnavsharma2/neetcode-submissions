class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        neg = False
        if x < 0:
            neg = True
        x= abs(x)
        while x > 0:
            digit = x %10
            rev = rev * 10 + digit
            x = x //10
        if not(-2**31 < rev < 2**31-1):
            return 0

        if neg:
            return -rev
        return rev
