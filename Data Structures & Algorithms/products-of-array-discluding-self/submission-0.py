class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n=len(nums)
        pref=[1]*n
        suff = [1]*n
        for i in range(1,len(nums)) :
            pref[i]=pref[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1) :
            suff[i]=suff[i+1]*nums[i+1]
        for i in range(len(nums)) :
            nums[i] = pref[i]*suff[i]
        return nums
        