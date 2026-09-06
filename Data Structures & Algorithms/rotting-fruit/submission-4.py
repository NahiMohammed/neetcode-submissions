class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        n = len(grid)
        m = len(grid[0])
        fresh=0

        for i in range(n) :
            for j in range(m) :

                if grid[i][j] == 2 :
                    rotten.append((i,j))

                elif grid[i][j]==1 :
                    fresh+=1

        directions = [(0,1) , (0,-1) , (1,0), (-1,0)]

        minutes=0

        while rotten and fresh >0:
            
            minutes+=1

            for _ in range(len(rotten)) :
                x,y = rotten.popleft()

                for dx , dy in directions :
                    nx,ny =x+dx,y+dy
                    if nx>=0 and nx<n and ny>=0 and ny<m :
                        if grid[nx][ny]==1 :
                            grid[nx][ny]=2
                            fresh-=1
                            rotten.append((nx,ny))
        return minutes if fresh ==0 else -1



 
        