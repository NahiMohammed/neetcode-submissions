class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        INF = 2**31 - 1
        for i in range(n) :
            for j in range(m) :
                if grid[i][j] == 0 :
                    q.append((i,j))
        distance = 1
        while q : 
            for _ in range(len(q)) :

                x,y = q.popleft()
                for dx, dy in directions :
                    nx , ny = x+dx , y+dy 
                    if nx>=0 and nx<n and ny>=0 and ny<m :
                        if grid[nx][ny] == INF :
                            grid[nx][ny] = distance 
                            q.append((nx,ny))
            distance+=1


                

        