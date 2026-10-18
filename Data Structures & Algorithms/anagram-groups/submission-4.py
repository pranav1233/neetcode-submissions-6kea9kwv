class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for word in strs:
            s = [0] * 26

            for ch in word:
                s[ord(ch) - ord('a')] += 1

            dic[tuple(s)].append(word)


        return list(dic.values())

            