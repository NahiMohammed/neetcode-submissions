class MedianFinder:

    def __init__(self):
        self.low = []   # max-heap (inversé)
        self.high = []  # min-heap

    def addNum(self, num: int):
        # 1. push dans low
        heapq.heappush(self.low, -num)
        

        # 2. équilibrer ordre entre heaps
        heapq.heappush(self.high, -heapq.heappop(self.low))

        

        # 3. garder low >= high en taille
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self):
        print("findmedian")
        print(self.low)
        print(self.high)
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2
        print("###################")