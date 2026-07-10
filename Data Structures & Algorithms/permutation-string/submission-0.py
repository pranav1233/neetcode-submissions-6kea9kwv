class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0

        for r,val in enumerate(s2):
            if val in s1:
                if r+len(s1) <= len(s2):
                    posi = s2[r:r+(len(s1))]

                    if sorted(posi) == sorted(s1):
                        return True
        
        return False