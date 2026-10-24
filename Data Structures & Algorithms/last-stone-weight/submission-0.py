class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for st in stones : 
            heapq.heappush(heap , -st)
        
        while len(heap)>=2 :
            a=-heapq.heappop(heap)
            b=-heapq.heappop(heap)
            if a>b :
                heapq.heappush(heap,b-a)
            elif b>a :
                heapq.heappush(heap,a-b)
        return -heap[0] if heap else 0 


            

        