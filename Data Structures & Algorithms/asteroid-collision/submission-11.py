class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        [2,4,-4,-1]
        [2]
        [-2,4,-4,-1]
        [-2,-1]
        """
        st=[]
        for a in asteroids :
            if a>0:
                st.append(a)
            else :
                if not st or st[-1]<0:
                    st.append(a)
                else :
                    destroid=False
                    while st and st[-1]>0 and not destroid :
                        last=st[-1]
                        if last>=-a :
                            destroid=True
                            if last==-a :
                                st.pop()
                        else :
                            st.pop()
                    if not destroid :
                        st.append(a)

        return st


        