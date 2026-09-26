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

        while stk and safeStack:
            if stk[-1][1] > safeStack[-1][1]:
                return False
            stk.pop()
            safeStack.pop()

        return not stk