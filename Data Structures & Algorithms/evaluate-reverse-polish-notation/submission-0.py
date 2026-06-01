class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for s in tokens : 
            if s.isdigit():
                st.append(int(s))
            elif s=="+" :
                st.append(st.pop()+st.pop())
            elif s=="*" :
                st.append(st.pop()*st.pop())
            elif s=="-" :
                st.append(-st.pop()+st.pop())
            elif s=="/" :
                st.append((1/st.pop())*st.pop())
            
        return st[-1]
            
                


        