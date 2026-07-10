class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res= 0 
        subs = {}

        for r in range(len(s)):
            subs[s[r]] = subs.get(s[r],0) + 1
            leng = r-l+1

            if leng - max(subs.values()) > k:
                subs[s[l]] -= 1
                l += 1

            res = max(res,r-l+1)

        return res