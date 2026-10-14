class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        s=set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        res= False
        n=len(board)
        m= len(board[0])

        def backtracking(i,j,idx_word) :
            nonlocal res
            if res :
                return
            if idx_word >= len(word) :
                res=True
                return 
            for dx, dy in directions :
                nx , ny = i+dx , j+dy 
                if nx>=0 and nx< n and ny >=0 and ny<m and (nx,ny) not in s and board[nx][ny]==word[idx_word]:
                    s.add((nx,ny))
                    backtracking(nx,ny,idx_word+1)
                    s.remove((nx,ny))

        
        for i in range(len(board)) :
            for j in range(len(board[0])) :
                if not res and board[i][j] == word[0] :
                    s.add((i,j))
                    backtracking(i,j , 1) 
                    s.remove((i,j))
        return res
