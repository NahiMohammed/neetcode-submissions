class MedianFinder:

    def __init__(self):
        self.heap=[]
        

    def addNum(self, num: int) -> None:
        print(self.heap)
        heapq.heappush(self.heap,num)
        

    def findMedian(self) -> float:
        if len(self.heap)%2==1 :
            return float(self.heap[len(self.heap)//2])
        return  (self.heap[len(self.heap)//2]+self.heap[len(self.heap)//2-1])/2
        