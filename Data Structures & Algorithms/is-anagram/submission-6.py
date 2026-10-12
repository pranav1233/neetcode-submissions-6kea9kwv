class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False 

        check = {}

        for ch in s:
            check[ch] = check.get(ch,0) + 1

        for ch in t:
            check[ch] = check.get(ch,0) - 1

        for values in check:
            if check[values] != 0:
                return False 

        return True