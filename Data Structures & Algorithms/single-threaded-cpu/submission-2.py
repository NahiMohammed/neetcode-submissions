class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        t=0
        res=[]
        available=[]
        heap_time = []
        heap_p = []

        for i, (enqueue, process) in enumerate(tasks):
            heapq.heappush(heap_time, (enqueue, process, i))


        while len(res)<len(tasks) :

            if not heap_p:
                t = max(t, heap_time[0][0])
            while heap_time and heap_time[0][0]<=t :
                t,t_p,idx =heapq.heappop(heap_time)
                heapq.heappush(heap_p,(t_p,t,idx))
           
            t_p,_,idx=heapq.heappop(heap_p)
            res.append(idx)
            t+=t_p



            
        return res


        