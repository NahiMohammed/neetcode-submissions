class Solution:
    def check(self, nums: List[int]) -> bool:
        m = min(nums)
        idx= 0
        for i in range(len(nums )) :
            if nums[i]==m :
                idx=i
                break
        for i in range(len(nums)-1) :
            if nums[(idx+i)%len(nums)]>nums[(idx+1+i)%len(nums)] :
                return False 

        return True
        