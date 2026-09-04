class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        n=len(matrix)
        m=len(matrix[0])
        
        tmp=[]
        for k in range((len(matrix)-1)//2+1):
            tmp=[]
            for i in range(k,n-k):
                tmp.append(matrix[k][i])
            res.extend(tmp)
            print(tmp)
            tmp=[]
            for i in range(k+1,n-k):
                res.append(matrix[i][n-k-1])
            tmp=[]
            for i in range(n-k-2,k-1,-1):
                res.append(matrix[n-k-1][i])
            tmp=[]
            for i in range(n-k-2,k,-1):
                res.append(matrix[i][k])
        return res
            


        

    """
    1  2  3  4 
    5  6  7  8
    9 10 11 12
    """
        