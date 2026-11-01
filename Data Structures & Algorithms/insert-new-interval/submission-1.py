import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        starts = [interval[0] for interval in intervals]
        idx = bisect.bisect_left(starts, newInterval[0])

        left = idx
        right = idx

        # Find leftmost overlapping interval
        for i in range(idx - 1, -1, -1):
            if intervals[i][1] >= newInterval[0]:
                left = i
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
            else:
                break

        # Find rightmost overlapping interval
        for i in range(idx, len(intervals)):
            if intervals[i][0] <= newInterval[1]:
                right = i + 1
                newInterval[1] = max(newInterval[1], intervals[i][1])
            else:
                break

        return intervals[:left] + [newInterval] + intervals[right:]