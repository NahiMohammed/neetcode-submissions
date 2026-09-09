class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        n=len(board)
        m=len(board[0])
        visited=set()

        def bfs(cord,i) :
            print(i)
            if i+1==len(word) :
                return True
            x,y =cord
            visited.add((x, y))
            for dx,dy in directions :
                nx=x+dx
                ny=y+dy
                if nx>=0 and nx<n and ny>=0 and ny<m and (nx,ny) not in visited:
                    if board[nx][ny] == word[i+1]: 
                        if bfs((nx,ny),i+1) :
                            return True
            visited.remove((x, y))
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]== word[0] :
                    visited.clear()
                    if bfs((i,j),0) :
                        
                        return True
        return False

        
                    
        