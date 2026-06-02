class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[asteroids[0]]
        for i in range(1,len(asteroids)) :

            if st and asteroids[i]*st[-1]>0 :
                st.append(asteroids[i])
            else :
                while st and asteroids[i]*st[-1]<0:
                    if abs(st[-1])>abs(asteroids[i]) :
                        break
                    elif abs(st[-1])==abs(asteroids[i]):
                        st.pop()
                        break
                    else:
                        st.pop()
                        st.append(asteroids[i])
            
        return st




        