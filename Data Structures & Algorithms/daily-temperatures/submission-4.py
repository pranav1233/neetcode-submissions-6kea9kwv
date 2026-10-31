class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] #[temp,index]

        for ind,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT,stackInd = stack.pop()
                res[stackInd] = ind - stackInd

            stack.append((temp,ind))

        return res
