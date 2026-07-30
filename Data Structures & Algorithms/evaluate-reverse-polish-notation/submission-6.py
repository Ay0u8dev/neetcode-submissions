class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n != '-' and n != '+' and n != '/' and n != '*':
                stack.append(n)
                continue
            y = stack.pop()
            x = stack.pop()
            stack.append(int(eval(f"{x} {n} {y}")))
        return int(stack[0]) 

        