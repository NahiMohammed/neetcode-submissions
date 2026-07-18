class KthLargest:
    #[2,3,3]

    def __init__(self, k: int, nums: List[int]):
        self.data=[]
        for i in nums :
            heapq.heappush(self.data,i)
        while len(self.data)>=k:
            heapq.heappop(self.data)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.data,val)
        return heapq.heappop(self.data)


        
