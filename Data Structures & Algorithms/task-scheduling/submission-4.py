import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        k = len(tasks)

        m = [""] * (k + (k - 1) * n)

        available = [1] * (k + (k - 1) * n)

        indices = [0] * len(m)
        for i in range(len(m)):
            indices[i] = i

        heapq.heapify(indices)

        for i, t in enumerate(tasks):

            if t not in dic:

                while indices and available[indices[0]] == 0:
                    heapq.heappop(indices)

                idx = heapq.heappop(indices)

                available[idx] = 0
                m[idx] = t
                dic[t] = idx

            else:

                while indices and available[indices[0]] == 0:
                    heapq.heappop(indices)

                idx1 = indices[0]
                idx2 = dic[t] + n + 1

                idx = max(idx1, idx2)

                available[idx] = 0
                m[idx] = t
                dic[t] = idx

        count = len(m)

        for i in range(len(m) - 1, -1, -1):
            if m[i] != "":
                count = i + 1
                break

        return count