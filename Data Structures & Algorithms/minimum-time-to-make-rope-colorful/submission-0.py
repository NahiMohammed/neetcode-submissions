class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0 
        i = 0 
        while i<len(colors) :
            j=i+1
            
            m = neededTime[i]
            s= m
            while j<len(colors) and colors[j] == colors[i] :
                s+=neededTime[j]
                if neededTime[j]>m : 
                    m = neededTime[j]

                j+=1
            
            res+=s-m
            i=j
        return res
            