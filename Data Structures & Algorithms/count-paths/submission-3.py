class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.res = 0
        self.dp(m,n,0,0)
        return self.res
    def dp(self, m: int, n: int,i:int,j:int):
        if i==m-1 and j==n-1 :
            self.res+=1
            return
        if i<m-1 :          
            self.dp(m,n,i+1,j)
        if j<n-1 :           
            self.dp(m,n,i,j+1)
        


        