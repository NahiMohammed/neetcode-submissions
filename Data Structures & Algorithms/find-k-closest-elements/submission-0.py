class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap =[]
        for i in range(len(arr)) :
            heapq.heappush(heap , (abs(arr[i]-x),arr[i] ))
        res=[]
        while len(res)<k :
            el=heapq.heappop(heap)
            res.append(el[1])
        res.sort()
        return res
        