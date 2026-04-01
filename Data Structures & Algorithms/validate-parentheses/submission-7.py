class Solution:
    def isValid(self, s: str) -> bool:
        ma= {')':'(' ,'}':'{' , ']':'['}
        add =[]
        

        for items in s:

            if items not in ma: 
                add.append(items)
            else: 
                if len(add) == 0:
                    return False 
                else: 
                    popp=add.pop()
                    if popp != ma[items]: 
                        return False 
        return not add