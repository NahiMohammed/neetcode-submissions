class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        res=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                idx=abs(grid[i][j])-1
                l=idx//n
                c=idx%n
                if grid[l][c]<0 :
                    res.append(idx+1)
                else :

                    grid[l][c]=-1*grid[l][c]
        for idx in range(0,n**2) :
            l=idx//n
            c=idx%n
            if grid[l][c]>0 :
                res.append(idx+1)
                break
        return res
        


[[-1,-2,-3,-4,-5,-6],
[-7,-8,-9,-10,-11,-12],
[-13,-14,-15,-16,-17,2],
[-19,20,21,22,23,24],
[25,26,27,28,29,30],
[31,32,33,34,35,36]]







        
[[-9,-1,-7]
,[-8,9,-2],
 [-3,-4,6]]