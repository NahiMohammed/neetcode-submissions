class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        while hand :
            m=min(hand)
            hand.remove(m)
            for i in range(groupSize-1) :
                if hand and m+1 in hand :
                    m+=1
                    hand.remove(m)
                else :
                    return False
        return not hand
        
        

        


        