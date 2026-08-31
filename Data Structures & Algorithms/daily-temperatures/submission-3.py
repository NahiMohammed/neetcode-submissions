class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        st=[]
        for i , t in enumerate(temperatures):
            while st and t>st[-1][1] :
                res[st[-1][0]]=i-st[-1][0]
                st.pop()
            st.append([i,t])
        return res
        