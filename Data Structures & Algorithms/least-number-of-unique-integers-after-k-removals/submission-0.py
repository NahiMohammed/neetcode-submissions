class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)

        heap =[]

        for n , fr in c.items() :

            heapq.heappush(heap,(fr,n)) 
        while  k>0:
            k-=1
            fr , n  = heapq.heappop(heap)
            fr -= 1
            if fr>0 :
                heapq.heappush(heap,(fr,n))
        return len(heap) 





