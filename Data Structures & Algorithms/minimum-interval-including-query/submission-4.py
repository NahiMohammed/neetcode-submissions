import bisect
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        n = len(queries)
        res = [-1] * n

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        heap = []
        for left, right in intervals:
            heapq.heappush(heap, (right - left + 1, left, right))

        while heap:
            length, left, right = heapq.heappop(heap)

            l = bisect.bisect_left(sorted_queries, (left, -1))
            r = bisect.bisect_right(sorted_queries, (right, n))

            j = find(l)

            while j < r:
                q, idx = sorted_queries[j]
                res[idx] = length

                # Mark this query as answered
                parent[j] = find(j + 1)

                j = find(j)

        return res