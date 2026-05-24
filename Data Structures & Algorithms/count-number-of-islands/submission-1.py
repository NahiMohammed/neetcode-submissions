from collections import deque

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        res = 0

        def bfs(i, j):
            q = deque([(i, j)])
            grid[i][j] = '0'

            while q:
                x, y = q.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        q.append((nx, ny))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    res += 1
                    bfs(i, j)

        return res