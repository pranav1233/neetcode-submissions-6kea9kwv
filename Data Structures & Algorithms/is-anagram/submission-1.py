class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        
        for ch in s:
            s_hash[ch] = s_hash.get(ch,0) + 1

        for ch in t:
            t_hash[ch] = t_hash.get(ch,0) + 1


        if len(s_hash) != len(t_hash):
            return False

        for items in s_hash:
            if items not in t_hash or s_hash[items] != t_hash[items]:
                return False 

        return True