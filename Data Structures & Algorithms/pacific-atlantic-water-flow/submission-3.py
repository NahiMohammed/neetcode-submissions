class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def pacific(i, j, visited):
            if (i, j) in visited:
                return False
            visited.add((i, j))

            if i == 0 or j == 0:
                return True

            for dx, dy in [(-1, 0), (0, -1),(0,1)]:
                nx, ny = i + dx, j + dy

                if 0 <= nx < len(heights) and 0 <= ny < len(heights[0]):
                    if heights[nx][ny] <= heights[i][j]:
                        if pacific(nx,ny,visited):
                            return True
            return False
        def atlantic(i, j, visited):
            if (i, j) in visited:
                return False

            visited.add((i, j))

            if i+1 == len(heights) or j+1 == len(heights[0]):
                return True

            for dx, dy in [(0,-1),(1, 0), (0, 1)]:
                nx, ny = i + dx, j + dy

                if 0 <= nx < len(heights) and 0 <= ny < len(heights[0]):
                    if heights[nx][ny] <= heights[i][j]:
                        if atlantic(nx,ny,visited):
                            return True
            return False


        res=[]
        r=len(heights)
        c=len(heights[0])
        for i in range(r):
            for j in range(c):
                if pacific(i,j,set()) and atlantic(i,j,set()) :
                    res.append([i,j])
        return res

        