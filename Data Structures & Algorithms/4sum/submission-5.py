class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=set()
        res1=[]
        for k in range(len(nums)-3):
            if k and nums[k]==nums[k-1]:
                    continue
            for i in range(k+1,len(nums)-2):
                l=i+1
                r=len(nums)-1
                while l<r :
                    s=nums[k]+nums[i]+nums[l]+nums[r]
                    if s==target and (nums[k],nums[i],nums[l],nums[r]) not in res :
                        res1.append([nums[k],nums[i],nums[l],nums[r]])
                        while l<r and nums[l+1]==nums[l]:
                            l+=1
                        while l<r and nums[r-1]==nums[r]:
                            r-=1
                        l+=1
                        r-=1
                    elif s>target :
                        r-=1
                    else :
                        l+=1

        return res1
        