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
        hold=None
        occ_hold =0
        while heap :
            print(heap)
            print(res)
            n , letter = heapq.heappop(heap)
            res.append(letter)
            n+=1
            if hold:
                heapq.heappush(heap, (occ_hold,hold))
                hold=None
                occ_hold=0

            if n !=0:
                if len(res)>=2 :
                    if res[-1]== letter and res[-2]==letter :
                        hold = letter 
                        occ_hold = n  
                    else :
                        heapq.heappush(heap,(n,letter))

                else :
                    heapq.heappush(heap,(n,letter))

        return "".join(res)
        