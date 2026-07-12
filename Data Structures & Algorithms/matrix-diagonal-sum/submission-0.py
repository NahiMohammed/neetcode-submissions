class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        for i in range(1,len(mat)):
            mat[0][0]+=mat[i][i]
        for j in range(len(mat)):
            if j!=len(mat)-j-1:
                mat[0][0]+=mat[j][len(mat)-j-1]
        return mat[0][0]
        