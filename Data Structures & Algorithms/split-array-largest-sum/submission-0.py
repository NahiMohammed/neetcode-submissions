class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        def condition(w):
            number_d = 1
            total=0

            for p in nums:
                total+=p
                if total>w :
                    total = p 
                    number_d+=1
                    if number_d>k :
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
        