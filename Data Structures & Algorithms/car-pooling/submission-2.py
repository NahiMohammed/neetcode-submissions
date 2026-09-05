class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_capacity=capacity
        stop=[]
        for t in trips :
            heapq.heappush(stop, [t[1],1,t[0]])
            heapq.heappush(stop, [t[2],0,t[0]])
        while stop :   
            _,pick , n =heapq.heappop(stop)
            if pick== 0 :
                curr_capacity+=n
            else :
                if curr_capacity<n :
                    return False
                else :
                    curr_capacity-=n
        return True

        