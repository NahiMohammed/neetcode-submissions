class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]

        for l in range(0,len(nums)-3):
            if l and nums[l]==nums[l-1] :
                continue
            for r in range(len(nums)-1,3,-1) :
                if r<len(nums)-1 and nums[r]==nums[r+1]:
                    continue

                l1=l+1
                r1=r-1
                while l1<r1 :
                    if nums[l1]+nums[r1]+nums[l]+nums[r]> target :
                        r1-=1
                    elif nums[l1]+nums[r1]+nums[l]+nums[r]< target:
                        l1+=1
                    else :
                        res.append([nums[l1],nums[r1],nums[l],nums[r]])
                        l1+=1
                        r1-=1
                        while (l1<r1) and nums[l1]==nums[l1-1]:
                            l1+=1
                        while (l1<r1) and nums[r1]==nums[r1+1]:
                            r1-=1
        return res
                        

                

        