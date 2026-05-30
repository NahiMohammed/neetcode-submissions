class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        s=set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    s.add((i,j))

        def update() :
            to_add = set()
            for (i,j) in s :
                for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)] :
                    nx , ny = i+dx , j+dy
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        to_add.add((nx, ny))
            return to_add
        res=0
        while True :
            new =update()
            if len(new)==0:
                if res==0:
                    return -1
                return res
            res+=1
            s.update(new)


        