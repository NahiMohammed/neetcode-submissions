class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num)==k : 
            return "0"

        st =[]
        for i , n  in enumerate(num) :
            if not st :
                if n !="0" :

                    st.append(n)
            else :
                if int(st[-1])>int(n) :
                    while k and st and st[-1]>n :
                        st.pop()
                        k-=1
                if n!="0" :
                    st.append(n)
                else :
                    if st :
                        st.append(n)
        while k and st:
            st.pop()
            k-=1


        return "".join(st) if st else "0"