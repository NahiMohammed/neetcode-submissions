class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<=r :
                s=nums[i]+nums[l]+nums[r]
                if s==0 :
                    res.append([nums[i], nums[l],nums[r]])
                l+=1
                r-=1
            


        return res
        nums=[-1,-1,0,1]
        