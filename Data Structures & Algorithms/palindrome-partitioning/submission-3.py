class Solution:
    def partition(self, s: str) -> List[List[str]]:
       
        temp, res = [],[]

        def backtrack(start):
            if start == len(s):
                res.append(temp[:])
                return 


            for i in range(start, len(s)):
                piece = s[start:i+1]

                if piece == piece[::-1]:
                    temp.append(piece)
                    backtrack(i+1)
                    temp.pop()

            
        backtrack(0)
        return res