class Solution:
    def minLength(self, s: str) -> int:
        st=[]
        for c in s :
            if c=="B" :
                if st and st[-1]=="A" :
                    st.pop()
                else: 
                    st.append(c)
            elif c=="D" :
                if st and st[-1]=="C" :
                    st.pop()
                else:
                    st.append(c)
            else :
                st.append(c)
            
        return len(st)
