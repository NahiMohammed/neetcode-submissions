class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        for x in path.split("/") :
            if x :
                if x==".":
                    continue
                elif x=="..":
                    if st:
                        st.pop()
                else :
                    st.append(x)
        return "/" + "/".join(st)

                

        