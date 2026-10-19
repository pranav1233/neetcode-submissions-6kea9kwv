class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for word in strs:
            ch = [0]*26

            for ltr in word:
                ch[ord(ltr) - ord('a')] += 1

            res[tuple(ch)].append(word)

        return list(res.values())