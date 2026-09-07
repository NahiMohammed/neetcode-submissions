class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0 
        right= len(nums)-1

        while left<right: 

            mid = left+ (right-left)//2
            if nums[left] <= nums[mid] :
                if  (target<nums[left] or target>nums[mid] ) :
                    left = mid + 1
                else :
                    right = mid

               
            else:
                if target <nums[mid] or target>nums[right] :

                    right = mid
                else :
                    left = mid

        return left if nums[left]==target else -1
        
        