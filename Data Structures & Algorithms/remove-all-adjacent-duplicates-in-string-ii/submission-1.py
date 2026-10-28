class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[]
        for i , c in enumerate(s) :
            st.append(c)
            if len(st)<k :
                continue    
            else :
                flag= False 
                for j in range(k) :
                    if st[-1-j]!=c :
                        flag = True
                        break
                if not flag :
                    for _ in range(k) :
                        st.pop()

        return "".join(st)



