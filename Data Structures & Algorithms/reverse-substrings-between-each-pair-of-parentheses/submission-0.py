class Solution:
    def reverseParentheses(self, s: str) -> str:
        st   = []
        for c in s :
            if c==")" :
                l = []
                while st[-1]!="(" :
                    e = st.pop()
                    l.append(e)
                st.pop()
                st.extend(l)
            else :
                st.append(c)
        return "".join(st)        


