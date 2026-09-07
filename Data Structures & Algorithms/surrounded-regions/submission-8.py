class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(x,y):
            nonlocal visited
            nonlocal safe
            visited.add((x,y))
            print(f"bfs called wiht (x,y))= {x,y }")
            for dx, dy in directions :
                nx =dx+x
                ny =dy+y
                if nx>=0 and nx<n and ny>=0 and ny<m and (nx,ny) not in visited:
                    if board[nx][ny]=="O" :
                        print("aaaaaa")
                        safe.append((nx,ny))
        
        visited=set()
        n=len(board)
        m = len(board[0])
        safe=deque()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(0,n):
            if board[i][0] == "O":
                safe.append(((i,0)))
            if board[i][m-1] == "O":
                safe.append(((i,m-1)))
        for j in range(1,m-1):
            if board[0][j] == "O":
                safe.append((0,j))
            if board[n-1][j] == "O":
                safe.append((n-1,j))
        
        while safe :
            print(safe)
            for _ in range(len(safe)) :
                x,y = safe.popleft()
                if (x,y) in visited :
                    continue
                else :
                    bfs(x,y)
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O" and (i,j) not in visited :
                    board[i][j]="X"


["O","X","X","O","X"],
["X","O","O","X","O"],
["X","O","X","O","X"],
["O","X","O","O","O"],
["X","X","O","X","O"]

        