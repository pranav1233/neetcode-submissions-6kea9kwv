class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        maxpro = 0 

        for r in range(1,len(prices)): 
            if prices[r] < prices [l]: 
                l = r
                r = r+1
            else: 
                maxpro = max(maxpro, (prices[r] - prices[l]))
                r +=1
        return maxpro