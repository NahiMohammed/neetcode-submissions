class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap_time = []
        heap_priority = []
        res = []
        time = 0

        for i, (enq, prc) in enumerate(tasks):
            heapq.heappush(heap_time, [enq, i, prc])

        while len(res) < len(tasks):

            while heap_time and time >= heap_time[0][0]:
                enq, idx, prc = heapq.heappop(heap_time)
                heapq.heappush(heap_priority, [prc, idx])

            if heap_priority:
                prc, idx = heapq.heappop(heap_priority)
                res.append(idx)
                time += prc

            else:
                time = heap_time[0][0]

        return res