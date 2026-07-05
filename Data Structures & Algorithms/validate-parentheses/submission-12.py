class Solution:
    def isValid(self, s: str) -> bool:
        valid = []
        combo = {")":"(","}":"{","]":"["}

        for p in s:
            if p not in combo:
                valid.append(p)
            else:
                if not len(valid) > 0:
                    return False
                pop = valid.pop()

                if pop != combo[p]:
                    return False

        return True if len(valid) == 0 else False