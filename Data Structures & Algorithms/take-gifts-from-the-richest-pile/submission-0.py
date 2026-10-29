class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for g in gifts :
            heapq.heappush(heap , -g)
        while k :
            g= - heapq.heappop(heap)
            k-=1
            heapq.heappush(heap , -int(sqrt(g)))
        return -sum(heap)
        