class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(x,y):
            nonlocal grid
            grid[x][y]="0"
            for dx,dy in directions :
                nx=x+dx
                ny=y+dy
                if nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]) and grid[nx][ny]=="1":
                    bfs(nx,ny)




        directions  = [(1,0),(0,1),(-1,0),(0,-1)]
        visited=set()
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1"  :
                    res+=1
                    bfs(i,j)

        return res
        
        