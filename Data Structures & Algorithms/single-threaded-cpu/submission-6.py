import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((e, p, i) for i, (e, p) in enumerate(tasks))

        res = []
        heap = []             
        t = 0
        i = 0
        n = len(tasks)

        while i < n or heap:

            if not heap:
                t = max(t, tasks[i][0])

            while i < n and tasks[i][0] <= t:
                enqueue, process, idx = tasks[i]
                heapq.heappush(heap, (process, idx))
                i += 1

            process, idx = heapq.heappop(heap)
            res.append(idx)
            t += process

        return res