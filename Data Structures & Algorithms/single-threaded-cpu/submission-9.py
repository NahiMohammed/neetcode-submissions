class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap=[]
        res=[]
        time=0
        heap_time=[]
        heap_priority=[]
        for i,t in enumerate(tasks):
            heapq.heappush(heap_time,[t[0]  , t[1] , i])
        


        while len(res)<len(tasks) :

            while heap_time and time>= heap_time[0][0] :
                enqtime, prc_time , idx = heapq.heappop(heap_time)
                heapq.heappush(heap_priority , [prc_time , enqtime , idx])
            if heap_priority : 
                prc_time , _ , idx = heapq.heappop(heap_priority) 
                res.append(idx)
                time+=prc_time
            else :
                time+=heap_time[0][0]

        return res

            
            


        