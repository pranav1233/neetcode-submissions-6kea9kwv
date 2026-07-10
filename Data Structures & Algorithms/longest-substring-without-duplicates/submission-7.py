class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0 
        subs = {}
        long = 0

        if len(s) == 0:
            return 0

        while r < len(s):
            if  s[r] in subs and subs[s[r]] >= l:
                l = subs[s[r]] + 1
            long = max(long,(r - l + 1))
            subs[s[r]] = r
            r += 1

        return long 
