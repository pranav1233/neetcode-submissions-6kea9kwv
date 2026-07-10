class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0 
        subs = {}
        long = 0 

        while r < len(s):
            if s[r] in subs and subs[s[r]] >= l:
                l = subs[s[r]] + 1
            subs[s[r]] = r
            long = max(long,(r - l + 1))
            r+=1

        return long