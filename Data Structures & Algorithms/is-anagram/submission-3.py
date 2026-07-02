class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def func(s):
            res = {}
            for ch in s:
                res[ch] = res.get(ch,0) + 1

            return res

        s_res = func(s)
        t_res = func(t)

        if len(t_res) != len(s_res):
            return False

        for items in s_res:
            if items not in t_res or t_res[items] != s_res[items]:
                return False

        return True