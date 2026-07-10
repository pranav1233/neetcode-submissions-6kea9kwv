class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        subs = {}
        res = 0 

        for ind,r in enumerate(s):
            if r in subs and subs[r] >= l:
                l = subs[r] + 1

            subs[r] = ind
            res = max(res,ind - l + 1)

        return res