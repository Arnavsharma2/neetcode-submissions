class Solution:
    def partition(self, s: str) -> List[List[str]]:

        path = []
        self.res = []

        def backtrack(start):
            if start == len(s):
                self.res.append(path.copy())

            for i in range(start, len(s)):
                nextP = s[start:i+1]
                if nextP != nextP[::-1]:
                    continue
                path.append(nextP)
                backtrack(i + 1)
                path.pop()
            
        backtrack(0)
        return self.res