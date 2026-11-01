class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        res=0
        n = len(intervals)
        last=0
        for i in range(1 , n) :
            if intervals[i][0]<intervals[last][1] :
                res+=1
            else :
                last = i
        return res
