class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(8):
            s=set()
            for j in range(8):
                if board[i][j]!="." and board[i][j] in s :
                    return False 
                else :
                    s.add(board[i][j])
        
        for j in range(8):
            s=set()
            for i in range(8):
                if board[i][j]!="." and board[i][j] in s :
                    return False 
                else :
                    s.add(board[i][j])
        
        for i in range(3) :
            for j in range(3):
                s=set()
                for l in range(3):
                    for m in range(3):
                        if board[3*i+l][3*j+m]!="." and board[3*i+l][3*j+m] in s :
                            return False 
                        else :
                            s.add(board[3*i+l][3*j+m])
        return True





        