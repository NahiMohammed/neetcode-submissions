class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(k):
            return sum((pile - 1) // k + 1 for pile in piles) <= h
        left= 1
        right = max(piles)
        while left<right :
            mid = left + (right-left)//2
            if condition(mid) :
                right= mid
            else :
                left = mid+1
        return left
