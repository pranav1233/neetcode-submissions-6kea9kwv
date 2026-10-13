class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = [] 

        temp = []
        def backtrack():
            if len(temp) == len(nums):
                res.append(temp[:])
                return 

            for num in nums:
                if num in temp:
                    continue
                elif num not in temp:
                    temp.append(num)
                    backtrack()
                    temp.pop()

        backtrack()

        return res