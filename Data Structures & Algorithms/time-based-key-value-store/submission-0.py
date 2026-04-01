class TimeMap:

    def __init__(self):
        self.items= {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.items: 
            self.items[key] = [] 
        self.items[key].append([value,timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.items.get(key,[])

        l,h = 0 , len(values) - 1 

        while l<=h: 
            m = l + ((h-l)//2)
            if values[m][1]<= timestamp: 
                res= values[m][0]
                l = m + 1
            else: 
                h = m - 1
        return res  

