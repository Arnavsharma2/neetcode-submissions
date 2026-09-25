class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        digitMap = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        res = []
        path = ''

        if digits == '':
            return []


        def dfs(i):
            nonlocal path
            if len(path) == len(digits):
                res.append(path)
                return
        
            for char in digitMap[digits[i]]:
                path += char
                dfs(i + 1)
                path = path[:-1]
        
        dfs(0)
        return res





        

