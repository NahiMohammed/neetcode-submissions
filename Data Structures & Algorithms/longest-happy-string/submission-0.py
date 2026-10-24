class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res=[]
        heap=[]
        if a :
            heapq.heappush(heap, (-a,"a"))
        if b :
            heapq.heappush(heap, (-b,"b"))
        if c :
            heapq.heappush(heap, (-c,"c"))
        hold = None

        while heap :
            freq , letter  = heapq.heappop(heap)
            freq+=1
            res.append(letter)
            if hold :
                heapq.heappush(heap , hold)
                hold = None
            if freq!=0 :
                if len(res)>=2 and res[-1]==letter and letter==res[-2] :
                    hold = (freq , letter)
                else :
                    heapq.heappush(heap,(freq,letter))

        
        return "".join(res)