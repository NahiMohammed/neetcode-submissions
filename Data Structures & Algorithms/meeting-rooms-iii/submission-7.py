class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])

        available = list(range(n))
        heapq.heapify(available)

        time = 0
        count = [0] * n
        room_available_at = []
        i = 0

        while i < len(meetings):
            meeting = meetings[i]
            time = meeting[0]

            while room_available_at and room_available_at[0][0] <= time:
                _, idx = heapq.heappop(room_available_at)
                heapq.heappush(available, idx)

            if available:
                idx = heapq.heappop(available)
                heapq.heappush(
                    room_available_at,
                    (time + (meeting[1] - meeting[0]), idx)
                )
                count[idx] += 1
                i += 1

            else:
                # Wait until a room becomes available
                earliest, idx = heapq.heappop(room_available_at)
                heapq.heappush(
                    room_available_at,
                    (earliest + meeting[1] - meeting[0], idx)
                )
                count[idx] += 1
                i += 1

        return count.index(max(count))