class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        freq=[[] for i in range(len(nums)+1)]
        res=[]

        for items in nums:
            dict[items] = 1+ dict.get(items,0)
        
        for n,c in dict.items():
            freq[c].append(n)

        for i in range((len(freq)-1),0,-1):
            for u in freq[i]:
                res.append(u)
                if len(res)== k:
                    return res 