class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        

        for l in range (len(temperatures)-1): 
            for r in range (l+1,len(temperatures)): 
                if temperatures[r] > temperatures[l]:
                    res.append(r-l)
                    break
            if len(res) == l+1: 
                continue
            else: 
                res.append(0)
        res.append(0)
        
        return res
