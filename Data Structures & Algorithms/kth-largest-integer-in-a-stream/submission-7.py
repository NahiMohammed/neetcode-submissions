class KthLargest:
    #[3,4,5,8]
    4

    def __init__(self, k: int, nums: List[int]):
        self.data=[]
        for i in nums :
            heapq.heappush(self.data,i)
        while len(self.data)>k:
            heapq.heappop(self.data)

        

    def add(self, val: int) -> int:
        heapq.heappush(self.data,val)
        heapq.heappop(self.data)
        return self.data[0]


        
