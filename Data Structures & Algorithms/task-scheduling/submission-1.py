class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap_cooldown = []
        heap_priority = []
        freq=Counter(tasks)
        cpu_cycle = 0

        for k, v in freq.items():
            heapq.heappush(heap_priority, (-v,k))

        while heap_priority or heap_cooldown :

            if not heap_priority :
                cpu_cycle = heap_cooldown[0][0]
            while heap_cooldown and cpu_cycle >=heap_cooldown[0][0] :
                t , freq , task =heapq.heappop(heap_cooldown)
                heapq.heappush(heap_priority,(freq,task))
            
            freq , task = heapq.heappop(heap_priority)
            freq+=1

            if freq<0 :
                heapq.heappush(heap_cooldown,(cpu_cycle+n+1,freq,task))

            cpu_cycle+=1
                




        return cpu_cycle

