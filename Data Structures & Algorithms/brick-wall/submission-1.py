
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        dic1 = defaultdict(int)

        for i in range(len(wall)):
            pos = 0
            for j in range(len(wall[i]) - 1):
                pos += wall[i][j]
                dic1[pos] += 1

        m = 0
        for k, v in dic1.items():
            if v > m:
                m = v

        return len(wall) - m
