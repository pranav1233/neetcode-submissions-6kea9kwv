class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sdic = defaultdict()
        tdic = defaultdict()

        if len(s) != len(t):
            return False

        for ch in s:
            sdic[ch] = sdic.get(ch,0) + 1

        for ch in t:
            tdic[ch] = tdic.get(ch,0) + 1

        for chars in sdic:
            if chars in tdic:
                if sdic[chars] != tdic[chars]:
                    return False
            else:
                return False

        return True

