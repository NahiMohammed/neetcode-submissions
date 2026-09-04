class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for k in range(n // 2):
            for i in range(k, n - k - 1):

                element = matrix[k][i]

                # top <- left
                matrix[k][i] = matrix[n - 1 - i][k]

                # left <- bottom
                matrix[n - 1 - i][k] = matrix[n - 1 - k][n - 1 - i]

                # bottom <- right
                matrix[n - 1 - k][n - 1 - i] = matrix[i][n - 1 - k]

                # right <- top
                matrix[i][n - 1 - k] = element