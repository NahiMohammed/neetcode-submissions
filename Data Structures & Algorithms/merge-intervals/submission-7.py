class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0])
        print(intervals)
        i  = 0 
        res= []
        while i <len(intervals) :
            slot = intervals[i]
            j = i+1
            while j<len(intervals) and intervals[j][0] <= slot[1] :
                j+=1
                slot[1]= max(intervals[j-1][1],slot[1])
            res.append(slot)
            i=j
        return res
        