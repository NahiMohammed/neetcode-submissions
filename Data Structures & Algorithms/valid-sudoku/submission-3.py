class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s=set()
        for i in range(9) :
            s.clear()
            for j in range(9):
                if board[i][j]=="."  :
                    continue
                if board[i][j] in s :
                    return False
                s.add(board[i][j])
        for i in range(9) :
            s.clear()
            for j in range(9):
                if board[j][i]=="."  :
                    continue
                if board[j][i] in s :
                    return False
                s.add(board[j][i])
        for i in range(3) :
            for l in range(3):
                s.clear()
                for j in range(3) :
                    for k in range(3):
                        if board[j+3*i][k+3*l]=="."  :
                            continue
                        if board[j+3*i][k+3*l] in s :
                            return False
                        s.add(board[j+3*i][k+3*l])
        return True

                    

        