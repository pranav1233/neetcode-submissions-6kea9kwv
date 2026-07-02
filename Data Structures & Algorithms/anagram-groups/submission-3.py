class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        
        for item in strs:
            key = [0]*26

            for ch in item:
                key[ord(ch) - ord("a")] += 1
            
            res[tuple(key)].append(item)

        return list(res.values())