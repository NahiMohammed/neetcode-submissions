class Solution:
    def climbStairs(self, n: int) -> int:
        if n in [1,2,3] :
            return n
        res=[0]*n
        res[0]=1
        res[1]=2
        for i in range(2,n):
            res[i]=res[i-1]+res[i-2]
        return res[n-1]
"""
res=[1,2,3,5,5]
1,1,1,1,1
1,1,1,2
1,1,2,1
1,2,1,1
1,2,2
2,1,1,1
2,1,2
2,2,1

"""