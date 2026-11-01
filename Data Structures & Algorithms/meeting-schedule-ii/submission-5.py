class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        heap = []

        for meeting in intervals:
            if heap and heap[0] <= meeting.start:
                heapq.heappop(heap)

            heapq.heappush(heap, meeting.end)

        return len(heap)