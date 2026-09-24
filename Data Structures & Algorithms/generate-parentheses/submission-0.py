class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.path = '('
        self.res = []


        def backtrack(openP, closedP):
            if openP == closedP and n*2 == len(self.path):
                self.res.append(self.path)

            if openP > closedP:
                self.path += ')'
                backtrack(openP, closedP+1)
                self.path = self.path[:-1]
            if openP < n:
                self.path += '('
                backtrack(openP + 1, closedP)
                self.path = self.path[:-1]
        
        backtrack(1, 0)
        return self.res
            



