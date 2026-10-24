class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap=[]
        res=[]
        for k , v in count.items():
            heapq.heappush(heap,(-v,k))
        prev = None


        while heap :
            freq , letter =heapq.heappop(heap)
            if prev :
                heapq.heappush(heap,(prev))
            
            res.append(letter)
            freq+=1
            if freq!=0 : 
                prev= (freq,letter)
            else :
                prev= None
        if prev :
            return ""    
        return "".join(res)