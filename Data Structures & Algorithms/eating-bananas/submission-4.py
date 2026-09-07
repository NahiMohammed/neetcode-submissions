class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def condition(rate):
            number_h = 0

            for p in piles:
                number_h += (p + rate - 1) // rate

            return number_h <= h

        while left < right:
            mid = left + (right - left) // 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left