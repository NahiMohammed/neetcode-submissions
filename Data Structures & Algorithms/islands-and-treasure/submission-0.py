class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(i,j):
            q = deque([(i, j)])
            while q :
                x, y = q.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny =x+dx,y+dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny]!=-1 and grid[nx][ny]!=0 :
                        if grid[x][y] + 1 < grid[nx][ny]:
                            grid[nx][ny] = grid[x][y] + 1
                            q.append((nx, ny))
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    bfs(i,j)
        
