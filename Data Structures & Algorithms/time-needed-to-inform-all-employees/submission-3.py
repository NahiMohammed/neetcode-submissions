from collections import deque, defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(list)
        for emp, boss in enumerate(manager):
            if boss != -1:
                children[boss].append(emp)

        q = deque([(headID, 0)])
        res = 0

        while q:
            emp, time = q.popleft()
            res = max(res, time)
            for child in children[emp]:
                q.append((child, time + informTime[emp]))

        return res