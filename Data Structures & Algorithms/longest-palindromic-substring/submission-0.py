class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        rind = 0
        rlen = 0 

        for i in range(len(s)):

            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > rlen:
                    rind = l
                    rlen = r - l + 1

                l -= 1
                r += 1

            l, r = i, i+1

            while l >= 0 and r< len(s) and s[l] == s[r]:
                if (r - l + 1) > rlen:
                    rind = l 
                    rlen = r - l + 1

                r += 1
                l -= 1

        return s[rind:rind+rlen]