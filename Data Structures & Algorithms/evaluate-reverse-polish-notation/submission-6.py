class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        res = 0
        sett = ("+","-","*","/")

        for items in tokens:
            if items not in sett:
                stack.append(items)
            else:
                s= int(stack.pop())
                f= int(stack.pop())
                if items == "+":
                    stack.append(f+s)
                elif items =="-":
                    stack.append(f-s)
                elif items =="*":
                    stack.append(f*s)
                elif items == "/":
                    stack.append(f/s)

        return int(stack[0])
