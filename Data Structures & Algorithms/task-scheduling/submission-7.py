class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        time=0 
        heap =[-freq for freq in count.values()]
        heapq.heapify(heap)

        cooldown=deque()
        while cooldown or heap :
            time+=1 
            while cooldown and cooldown[0][1]<time :
                freq , _ = cooldown.popleft()
                heapq.heappush(heap ,freq )

            if heap : 
                freq= heapq.heappop(heap)
                freq+=1
                if freq<0 :
                    cooldown.append([freq,time+n])
                

        return time


        