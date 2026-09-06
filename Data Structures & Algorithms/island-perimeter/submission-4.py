class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        start=(0,0)
        for i in range(n):
            for j in range(m) :
                if grid[i][j]==1 :
                    start=(i,j)
                    break
        print(start)
        res=0
        directions = [(0,1),(0,-1), (1,0) ,(-1,0)]
        visited=set()
        queu=deque([start])
        while queu :
            x,y = queu.popleft()
            visited.add((x,y))
            for dx, dy in directions :
                nx, ny =dx+x,dy+y
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    if nx<0 or nx>=n :
                        res+=1
                    elif ny<0 or ny>=m :
                        res+=1
                else   :
                    if grid[nx][ny]==1:
                        if (nx,ny) not in visited :
                            queu.append((nx,ny))
                    else :
                        res+=1
        return res



        