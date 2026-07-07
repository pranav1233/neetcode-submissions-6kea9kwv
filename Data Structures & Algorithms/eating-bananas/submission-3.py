class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        k = float("inf")
        
        while l <= r:
            m = l+((r-l)//2)
            time = 0
            for items in piles:
                time += math.ceil(items/m)
            if time > h:
                l = m + 1
            elif time <= h: 
                r = m - 1 
                k = min(k,m)
            
        return k 