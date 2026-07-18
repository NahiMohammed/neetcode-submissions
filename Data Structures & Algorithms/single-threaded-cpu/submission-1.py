class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        t = 0
        res = []
        heap_time = []
        heap_p = []

        for i, (enqueue, process) in enumerate(tasks):
            heapq.heappush(heap_time, (enqueue, process, i))

        while len(res) < len(tasks):

            # S'il n'y a aucune tâche disponible, on saute directement
            if not heap_p:
                t = max(t, heap_time[0][0])

            while heap_time and heap_time[0][0] <= t:
                enqueue, process, idx = heapq.heappop(heap_time)
                heapq.heappush(heap_p, (process, idx))

            process, idx = heapq.heappop(heap_p)
            res.append(idx)
            t += process

        return res