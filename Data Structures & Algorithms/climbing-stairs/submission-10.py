class Solution:
    def climbStairs(self, n: int) -> int:
        res=0
        
        def backtracking(i):
            nonlocal res
            if i==n :
                res+=1
                return 
            if i>n :
                return
            backtracking(i+1)
            backtracking(i+2)
        backtracking(0)
        return res
        


        