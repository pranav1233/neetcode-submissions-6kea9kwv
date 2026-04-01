class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        res=0

        for items in tokens: 
            if items not in ['+','-','*','/']: 
                st.append(int(items))
            else: 
                firpop = int(st.pop())
                secpop = int(st.pop())
                if items == '+': 
                    res = int(firpop)+int(secpop) 
                if items == '-': 
                    res = int(secpop)-int(firpop) 
                if items == '*': 
                    res = int(firpop)*int(secpop) 
                if items == '/': 
                    res = int(secpop)/int(firpop) 
                st.append(res)
        return int(st[0])