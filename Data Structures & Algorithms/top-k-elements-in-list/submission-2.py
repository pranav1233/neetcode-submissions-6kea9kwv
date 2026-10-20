class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            res[num] = res.get(num,0) + 1

        for val, cnt in res.items():
            freq[cnt].append(val)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res