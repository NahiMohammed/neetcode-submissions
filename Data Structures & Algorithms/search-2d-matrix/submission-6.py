class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        left=0
        right = n*m-1
        while left<right :
            mid= left + (right-left)//2
            if target<=matrix[mid//m][mid%m] :
                right= mid
            else :
                left=mid+1
        print(left)
        if left == n*m :
            return False
        return True if matrix[left//m][left%m]==target  else  False
        