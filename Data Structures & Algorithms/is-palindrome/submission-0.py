class Solution:
    def isPalindrome(self, s: str) -> bool:
        import math 
        

        j = ''.join(e for e in s.lower() if e.isalnum())
        l,r = 0 , (len(j)-1)

        while r >= math.ceil(len(j)/2): 
            if j[l] != j[r]: 
                return False 
            l+=1 
            r-=1
        return True 