class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for st in strs:
            res.append(str(len(st)))
            res.append("#")
            res.append(st)

        return "".join(res)


    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i 
            while s[j] != "#":
                j+=1
            lenght = int(s[i:j])

            i = j+1
            j = i+lenght

            res.append(s[i:j])
            i=j

        return res