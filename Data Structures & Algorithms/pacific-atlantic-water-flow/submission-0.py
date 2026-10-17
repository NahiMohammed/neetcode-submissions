class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(heights)
        m = len(heights[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def pacific(i, j, visited):
            if i < 0 or j < 0:
                return True

            visited.add((i, j))

            for dx, dy in directions:
                nx = i + dx
                ny = j + dy

                if nx < 0 or ny < 0:
                    return True

                if (0 <= nx < n and 0 <= ny < m
                    and (nx, ny) not in visited
                    and heights[nx][ny] <= heights[i][j]):
                    if pacific(nx, ny, visited):
                        return True

            return False

        def atlantic(i, j, visited):
            if i >= n or j >= m:
                return True

            visited.add((i, j))

            for dx, dy in directions:
                nx = i + dx
                ny = j + dy

                if nx >= n or ny >= m:
                    return True

                if (0 <= nx < n and 0 <= ny < m
                    and (nx, ny) not in visited
                    and heights[nx][ny] <= heights[i][j]):
                    if atlantic(nx, ny, visited):
                        return True

            return False

        for i in range(n):
            for j in range(m):
                if pacific(i, j, set()) and atlantic(i, j, set()):
                    res.append([i, j])

        return res