class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left = 0
        right = mountainArr.length() - 1

        while left < right:
            mid = left + (right - left) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left
        left = 0
        right = peak

        while left < right:
            mid = left + (right - left) // 2
            if mountainArr.get(mid) >= target:
                right= mid
            else:
                left= mid+1
        if mountainArr.get(left)==target :
            return left
        
        left = peak+1
        right = mountainArr.length() - 1

        while left < right:
            mid = left + (right - left) // 2
            if mountainArr.get(mid) <= target:
                right= mid
            else:
                left= mid+1
        if mountainArr.get(left)==target :
            return left
        else :
            return -1
        