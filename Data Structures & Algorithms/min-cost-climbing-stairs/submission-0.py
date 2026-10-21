class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        arr = [0] * len(cost)
        arr[-1] = cost[-1]
        arr[-2] = cost[-2]


        if len(cost) > 2:
            for i in range(len(cost)-3,-1,-1):
                
                if arr[i+1] < arr[i+2]:
                    arr[i] = cost[i] + arr[i+1]
                else: 
                    arr[i] = cost[i] + arr[i+2]

            
        return arr[0] if arr[0] < arr[1] else arr[1]

