class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int :
        if len(piles)==1 :
            return piles[0]//h+1
        left= 1
        right = sum(piles)
        def condition(rate) :

            number_h=0
            for p in piles :
                while p>0:
                    p-=rate
                    number_h+=1

            return True if number_h<=h else False

        while left <right :
            mid=left+(right-left)//2
            if condition(mid) :
                
                right=mid
            else :
                left=mid+1
        return left

        