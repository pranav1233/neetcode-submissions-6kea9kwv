class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        arr = [0] * len(cost)
        arr[0] = cost[0]
        arr[1] = cost[1]


        if len(cost) > 2:
            for i in range(2,len(cost)):
                
                if arr[i-1] < arr[i-2]:
                    arr[i] = cost[i] + arr[i-1]
                else: 
                    arr[i] = cost[i] + arr[i-2]

            
        return arr[-1] if arr[-1] < arr[-2] else arr[-2]

