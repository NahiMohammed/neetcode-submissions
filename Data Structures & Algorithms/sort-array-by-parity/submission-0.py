class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0 
        r = len(nums)-1

        while l<r and nums[r]%2 == 1 :
            r-=1
        while l<r and nums[l]%2 == 0 :
            l+=1
        
        while l<r  :
            nums[r] , nums[l] = nums[l] , nums[r]
            while l<r and nums[r]%2 == 1 :
                r-=1
            while l<r and nums[l]%2 == 0 :
                l+=1
        return nums