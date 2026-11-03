class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        counter = Counter(hand)
        while len(counter)>=groupSize :
            m = min(counter.keys())
            occ = counter[m]
            del counter[m]
            for i in range(1,groupSize) :
                if counter[m+i]<occ :
                    return False
                counter[m+i]-=occ
                if counter[m+i]==0 :
                    del counter[m+i]
                



            
        
        return True if len(counter)==0 else False
        