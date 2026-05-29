class MedianFinder:

    def __init__(self):
        self.heap=[]
        

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.heap,num)
        print(self.heap)
        

    def findMedian(self) -> float:
        if len(self.heap)%2==1 :
            return float(self.heap[len(self.heap)//2])
        return  (self.heap[len(self.heap)//2]+self.heap[len(self.heap)//2-1])/2
        