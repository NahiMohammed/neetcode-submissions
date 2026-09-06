class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        start=deque()
        n=len(grid)
        m=len(grid[0])    
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0 :
                    start.append((i,j))
        visited=set()
        directions = [(1,0) , (-1,0) , (0,1) , (0 , -1)]
        step=0
        while start :
            step+=1
            for _ in range(len(start)):

                (x,y) = start.popleft()

                for dx, dy in directions :

                    nx , ny = x+dx , y+dy 

                    if nx>=0 and nx<n and ny >=0 and ny <m :
                        if (nx,ny) not in visited :
                            if grid[nx][ny]!= 0 and grid[nx][ny]!=-1 :
                                grid[nx][ny]=min(grid[nx][ny],step)
                                start.append((nx,ny))
                                visited.add((nx,ny))
        

        