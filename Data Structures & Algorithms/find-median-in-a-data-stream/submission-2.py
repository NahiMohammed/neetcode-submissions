class MedianFinder:

    def __init__(self):
        self.upper = []
        self.lower = []

        #lower is heap max 
        #upper id heap low 

    def addNum(self, num: int) -> None:
        if not self.lower or num<-self.lower[0]:
            heapq.heappush(self.lower,-num)
        else :
            heapq.heappush(self.upper , num)


        if  len(self.lower)>len(self.upper)+1 :
            top = - heapq.heappop(self.lower)
            heapq.heappush(self.upper,top)

        if  len(self.lower)<len(self.upper) :
            top = heapq.heappop(self.upper)
            heapq.heappush(self.lower,-top)


        

    def findMedian(self) -> float:
        if len(self.lower)>len(self.upper):
            return float(-self.lower[0])
        else :
            return ((-self.lower[0]+self.upper[0])/2)
        
        