class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for s in tokens : 
            if s.isdigit():
                st.append(int(s))
            elif s=="+" :
                st.append(st.pop()+st.pop())
            elif s=="*" :
                a=st.pop()
                b=st.pop()
                
                st.append(a*b)
            elif s=="-" :
                st.append(-st.pop()+st.pop())
            elif s=="/" :
                a=st.pop()
                b=st.pop()
                st.append(b//a)
            
        return st[-1]
            
                


        