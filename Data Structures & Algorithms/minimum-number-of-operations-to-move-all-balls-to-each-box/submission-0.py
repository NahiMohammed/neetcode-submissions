class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res=[0]*len(boxes)
        n=len(boxes)
        
        s=0
        for i in range(n) :
            for j in range(n) :
                if i!=j and boxes[j]=="1" :
                    res[i]+= abs(j - i) 
        return res

        