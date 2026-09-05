class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap_time = []
        heap_priority = []
        res = []
        time = 0

        # Put all tasks in the first heap
        for i, t in enumerate(tasks):
            heapq.heappush(heap_time, [t[0], t[1], i])

        # Process all tasks
        while len(res) < len(tasks):

            # Move all available tasks to priority heap
            while heap_time and time >= heap_time[0][0]:
                enqtime, prc_time, idx = heapq.heappop(heap_time)

                heapq.heappush(
                    heap_priority,
                    [prc_time, enqtime, idx]
                )

            # Execute the highest priority available task
            if heap_priority:
                prc_time, _, idx = heapq.heappop(heap_priority)

                res.append(idx)
                time += prc_time

            # No task available: jump to next enqueue time
            else:
                time = heap_time[0][0]

        return res