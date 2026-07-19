class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        print(c)
        heap =[[-int(fr) , x] for x ,fr in c.items()]
        heapq.heapify(heap)
        dq=deque()
        time =0 
        while heap or dq:
            if not heap :
                time =max(time,dq[0][0])
            while dq and dq[0][0] <= time:
                t, fr, x = dq.popleft()
                heapq.heappush(heap,[fr,x])
            fr,x = heapq.heappop(heap)
            
            fr+=1
            if fr<0 : 
                dq.append((time+n+1,fr,x))


            time+=1


        return time
        