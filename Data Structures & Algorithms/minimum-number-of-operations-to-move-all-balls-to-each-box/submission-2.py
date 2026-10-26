class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        pref = [0]*n
        suff = [0]*n

        curr_ball = 1 if boxes[0]=="1" else 0 
        for i in range(1,len(boxes)) :

            pref[i] += pref[i-1]+curr_ball
            if boxes[i] == "1" :
                curr_ball+=1

        curr_ball = 1 if boxes[-1]=="1" else 0 
        for i in range(len(boxes)-2,-1,-1) :

            suff[i] += suff[i+1]+curr_ball
            if boxes[i] == "1" :
                curr_ball+=1

        return [suff[i] + pref[i] for i in range(n)]
