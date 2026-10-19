class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res, temp = [], []

        visited = []

        def backtrack():
            if len(temp) == len(nums):
                res.append(temp[:])
                return

            for num in nums:
                if num in temp:
                    continue

                temp.append(num)
                visited.append(num)
                backtrack()
                temp.pop()
                visited.remove(num)

        backtrack()
        return res