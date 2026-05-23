class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res= [0]*len(temperatures)
        st=[]
        for i , t in enumerate(temperatures):
            while(st and t>st[-1][1]):
                ind,t_ind =st.pop()
                res[ind]=i-ind
            st.append((i,t))
        
        return res 
        