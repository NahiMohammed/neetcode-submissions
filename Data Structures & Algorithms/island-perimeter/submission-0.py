class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        n=len(grid)
        m=len(grid[0])
        res=0
        visited=set()
        def bfs(i,j) :
            nonlocal res 
            visited.add((i,j))

            for dx , dy in directions :
                nx , ny = dx+i , dy +j
                if not (nx>=0 and nx<n and  ny>=0 and ny<m) :
                    res+=1
                else :
                    if grid[nx][ny]==0 :
                        res+=1
                    else :
                        if (nx,ny) not in visited :

                            bfs(nx,ny)



        flag= False
        for i in range(len(grid)) :
            if flag  :
                break
            for j in range(len(grid[0])) :
                
                if grid[i][j]==1 :
                    flag= True
                    bfs(i,j)
                    break
        return res