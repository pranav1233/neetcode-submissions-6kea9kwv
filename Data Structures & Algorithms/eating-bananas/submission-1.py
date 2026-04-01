class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        low = 1 
        high = max(piles)
        res = high 
         
        if len(piles) > 1: 
            while low <= high : 
                mid = low + ((high-low)//2)
                tot = 0
                for num in piles: 
                    tot = tot + math.ceil(num/mid)
                if tot > h : 
                    low = mid + 1 
                elif tot <= h:
                    res = min(res,mid) 
                    high = mid - 1 
                
        else : 
            return math.ceil(piles[0]/h)

        return res