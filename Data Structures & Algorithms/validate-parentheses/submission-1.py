class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        match = {"{":"}", "[":"]", '(':')'}

        for char in s:
            if char in match:
                stk.append(match[char])
            elif stk and char == stk[-1]:
                stk.pop()
            else:
                return False
        return stk == []