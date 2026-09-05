class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap=[]
        res=[]
        for k , v in count.items():
            heapq.heappush(heap,(-v,k))
        prev = None
        prev_occ= 0
        while heap :
            freq , letter =heapq.heappop(heap)
            if prev :
                if heap :

                    heapq.heappush(heap,(prev_occ,prev))
                else :
                    return ""
            if res and res[-1]==letter :
                prev=letter
                prev_occ=freq



            else : 
                res.append(letter)
                freq+=1
                if freq!=0 : 
                    heapq.heappush(heap,(freq,letter))
         
        return "".join(res)