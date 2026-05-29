class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []  # max heap simulé avec distances négatives

        for x, y in points:
            dist = x*x + y*y  # pas besoin de sqrt

            # push en négatif pour simuler max heap
            heapq.heappush(heap, (-dist, x, y))

            # garder seulement k éléments
            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, x, y in heap]
        