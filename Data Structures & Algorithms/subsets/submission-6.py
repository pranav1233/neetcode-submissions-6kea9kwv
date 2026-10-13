class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            newsub = []
            for cur in res:
                newsub.append(cur+[num])
            res.extend(newsub)

        return res