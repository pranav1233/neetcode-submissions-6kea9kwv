class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = {}
        freq = [[] for _ in range(len(nums) + 1)]
        output = []

        for num in nums:
            res[num] = res.get(num,0) + 1

        for key, val in res.items():
            freq[val].append(key)

        for i in range(len(freq) - 1, 0, -1):
            for that in freq[i]:
                output.append(that)
                if len(output) == k:
                    return output

                
            