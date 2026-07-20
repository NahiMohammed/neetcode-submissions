class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q=deque(tickets)
        t=0
        while q[k]>1 :
            #print(q , k)
            p=q.popleft()
            p-=1
            if p>=1 :

                q.append(p)

            k-=1
            if k<0 :
                k=len(q)-1
            t+=1
        return t+len(q)
        """
        5111 0
        1114 3
        114 2
        14 1
        4 0
        3 0
        2 0
        1 
        """
        