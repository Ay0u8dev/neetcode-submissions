class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            print(stack)
            if n != '-' and n != '+' and n != '/' and n != '*':
                stack.append(n)
                continue
            y = stack.pop()
            x = stack.pop()
            # if n == '/':
            #     if y == 0:
            #         return 0
            #     stack.append(int(eval(f"{x} / {y}")))
            #     continue
            stack.append(int(eval(f"{x} {n} {y}")))
        return int(stack[0]) 

        