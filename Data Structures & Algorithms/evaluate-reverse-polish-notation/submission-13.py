class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        if len(tokens) <= 2:
            return int(tokens[-1])

        oper = {"+","-","*","/"}

        for vals in tokens:
            if vals not in oper:
                stack.append(vals)

            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if vals == "+":
                    stack.append(first+second)
                elif vals == "-":
                    stack.append(first-second)
                elif vals == "*":
                    stack.append(first*second)
                elif vals =="/":
                    stack.append(int(float(first) / second))

        return stack[-1]