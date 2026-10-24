class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap_stop = []
        # -1  mean i get to drop passanger
        # 1 mean i have to get passanger
        for i, tr in enumerate(trips): 
            heapq.heappush(heap_stop , (tr[1],1,tr[0]))
            heapq.heappush(heap_stop , (tr[2],-1,tr[0]))
        while heap_stop :
            _,flag,number = heapq.heappop(heap_stop)
            if flag< 0 :
                capacity+=number
            else: 
                capacity-=number
                if capacity<0 :
                    return False
        return True
        

        