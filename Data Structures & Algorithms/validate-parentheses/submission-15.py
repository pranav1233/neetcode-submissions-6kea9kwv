class Solution:
    def isValid(self, s: str) -> bool:
        
        valid = {")":"(", "}":"{", "]":"["}

        if len(s) <= 1:
            return False

        stack = []

        for brac in s:
            if brac not in valid:
                stack.append(brac)
            else:
                if len(stack) == 0:
                    return False
                else:
                    popp = stack.pop()
                    if popp != valid[brac]:
                        return False

        return True if not stack else False