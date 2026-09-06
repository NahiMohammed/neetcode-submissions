class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            grid[x][y] = "0"
            area = 1

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]) and grid[nx][ny] == "1":
                    area += bfs(nx, ny)

            return area

        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    area = bfs(i, j)
                    res = max(res, area)

        return res