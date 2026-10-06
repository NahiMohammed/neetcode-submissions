class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res=0
        occ=Counter(heights)
        idx = len(heights)-1
        for i in range(100,0,-1) :
            if i not in occ :
                continue
            else :
                for j in range(occ[i]): 
                    if heights[idx]!=i :
                        res+=1
                    idx-=1
        return res
             

        