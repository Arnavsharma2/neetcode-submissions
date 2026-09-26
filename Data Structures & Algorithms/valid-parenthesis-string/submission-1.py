class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        safeStack = []

        for i in range(len(s)):
            char = s[i]
            if char == '*':
                safeStack.append(('*', i))
            elif char == '(':
                stk.append(('(', i))
            elif char == ")":
                if stk and stk[0][0] == '(':
                    stk.pop()
                elif safeStack:
                    safeStack.pop()
                else:
                    return False
        
        for char, i in stk:
            for star, j in safeStack:
                if j > i:
                    stk.remove((char, i))
                    safeStack.remove((star, j))
                    break

        return not stk