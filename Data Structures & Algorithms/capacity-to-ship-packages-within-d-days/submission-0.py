class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        def condition(w):
            number_d = 1
            total=0

            for p in weights:
                total+=p
                if total>w :
                    total = p 
                    number_d+=1
                    if number_d>days :
                        return False
            return True

            return number_h <= h

        while left < right:
            mid = left + (right - left) // 2

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left
        