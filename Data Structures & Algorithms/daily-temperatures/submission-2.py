class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures) :
            while st and t>temperatures[st[-1]]:
                idx=st.pop()
                res[idx]=i-idx
            st.append(i)
        return res



        