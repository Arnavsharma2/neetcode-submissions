class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return tokens[0]
        
        stk = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stk.append(token)
            else:
                num1 = int(stk.pop())
                num2 = int(stk.pop())
                if token == "+":
                    result = num1 + num2
                elif token == "-":
                    result = num1 - num2
                elif token == "*":
                    result = num1 * num2
                elif token == "/":
                    result = num1 // num2
                stk.append(result)
        
        return stk.pop()