class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(x,y):
            nonlocal edge
            nonlocal on_hold
            
            visited.add((x,y))
            if edge :
                return 
            on_hold.add((x,y))
            for dx, dy in directions :
                nx =dx+x
                ny =dy+y
                if nx<0 or nx>=n or ny<0 or ny>=m :
                    on_hold.clear() 
                    edge=True                   
                    return 
                else :
                    if board[nx][ny]=="0" :
                        bfs(nx,ny)
            if not edge :
                for (x,y) in on_hold :
                    board[x][y]="X"
        visited=set()
        n=len(board)
        m = len( board[0])
        on_hold=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        edge=False
        for i in range(n):
            for j in range(m) :
                if board[i][j]=="O" :
                    if (i,j) not in visited :
                        on_hold=set()
                        edge=False
                        bfs(i,j)

            

["O","X","X","O","X"],
["X","O","O","X","O"],
["X","O","X","O","X"],
["O","X","O","O","O"],
["X","X","O","X","O"]



        