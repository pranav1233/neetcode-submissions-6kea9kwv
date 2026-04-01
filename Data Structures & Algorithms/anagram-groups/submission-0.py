class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for items in strs:
            stor = [0]*26

            for ch in items:
                stor[ord(ch)-ord("a")] += 1 
            
            dict[tuple(stor)].append(items)

        return list(dict.values())