class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        n=len(matrix)
        m=len(matrix[0])
        print(m)
        tmp=[]
        for k in range((min(m,n)-1)//2+1):
            tmp=[]
            for i in range(k,m-k):
                tmp.append(matrix[k][i])
            res.extend(tmp)
            print(tmp)
            tmp=[]
            for i in range(k+1,n-k):
                tmp.append(matrix[i][m-k-1])
            res.extend(tmp)
            print(tmp)
            tmp=[]
            if n - k - 1 == k:
                break

            for i in range(m-k-2,k-1,-1):
                tmp.append(matrix[n-k-1][i])
            res.extend(tmp)
            print(tmp)
            tmp=[]
            if m - k - 1 == k:
                break
            for i in range(n-k-2,k,-1):
                tmp.append(matrix[i][k])
            res.extend(tmp)
            print(tmp)
        return res
            
    """
    1  2  3  4 
    5  6  7  8
    9 10 11 12
    """
        





