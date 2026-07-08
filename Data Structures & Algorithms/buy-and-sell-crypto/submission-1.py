class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l,r = 0, 1 
        max_pro = 0
        while r < len(prices):
            print (l,r)
            if prices[r] < prices[l]:
                l = r
                r += 1
                print(l,r)
                continue

            profit = prices[r] - prices[l]
            #print("profit: ",profit)
            max_pro = max(max_pro,profit)
            #print("max_pro: ", max_pro)
            r += 1

        return max_pro