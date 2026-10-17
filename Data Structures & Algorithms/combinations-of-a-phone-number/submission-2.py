class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res, temp = [], []

        if len(digits) == 0:
            return []

        mapping = {"2": ['a','b','c'],"3": ['d','e','f'],"4": ['g','h','i'],"5":['j','k','l'],"6": [ 'm','n','o'],"7": ['p','q','r','s'], "8": ['t','u','v'], "9":['w','x','y','z']}

        def backtrack(i):
            if i == len(digits):
                res.append("".join(temp))
                return 

            for char in mapping[digits[i]]:
                temp.append(char)
                backtrack(i+1)
                temp.pop()


        backtrack(0)

        return res