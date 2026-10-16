class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        q = deque([(sr,sc)])
        visited=set()
        n=len(image)
        m =len(image[0])
        original = image[sr][sc]
        while q  :
            x,y = q.popleft()
            visited.add((x,y))
            for dx , dy in directions :
                nx,ny = x+dx , y+dy
                if nx>=0 and ny>=0 and nx<n and ny<m and (nx,ny) not in visited and image[nx][ny] == original:

                    image[nx][ny] = color
                    q.append((nx,ny))
        image[sr][sc]=color

        return image


        
        