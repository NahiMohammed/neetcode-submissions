class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            if i and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r :
                s=nums[i]+nums[l]+nums[r]
                if s==0 :
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l+1]==nums[l]:
                        l+=1
                    while l<r and nums[r-1]==nums[r]:
                        r-=1
                    l+=1
                    r-=1
                elif s>0 :
                    r-=1
                else :
                    l+=1

        return res
        #nums=[-2,0,0,2,2]