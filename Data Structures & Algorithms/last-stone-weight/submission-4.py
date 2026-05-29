class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for st in stones :
            heapq.heappush(heap,-st)
        while len(heap)>1:
            a=heapq.heappop(heap)
            b=heapq.heappop(heap)
            if a!=b :
                heapq.heappush(heap,-abs(a-b))

        if len(heap):
            return -heap[0]
        return 0

            
        