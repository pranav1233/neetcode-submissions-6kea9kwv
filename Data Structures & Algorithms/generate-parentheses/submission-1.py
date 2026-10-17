class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        temp, res = [], [] 

        def backtrack(op,cp):
            if len(temp) == 2*n:
                res.append("".join(temp))
                return 

            if op < n:
                temp.append("(")
                backtrack(op+1,cp)
                temp.pop()

            if cp < op:
                temp.append(")")
                backtrack(op,cp+1)
                temp.pop()

            
        backtrack(0,0)
        return res
