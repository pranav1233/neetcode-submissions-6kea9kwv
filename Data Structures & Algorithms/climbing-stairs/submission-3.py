class Solution:
    def climbStairs(self, n: int) -> int:
        
        arr = [1,2]
        for i in range(2,n):
            summ = arr[i - 1] + arr[i - 2]
            arr.append(summ)

        return arr[-1] if n > 1 else 1

        

            