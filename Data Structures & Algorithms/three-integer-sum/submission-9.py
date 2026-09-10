class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res=[]
        print(nums)
        for l in range(0,len(nums)-2) :
            if l and nums[l]==nums[l-1]: 
                continue
            r=len(nums)-1
            s=nums[l]+nums[r]
            l1=l+1
            target = -s
            while r>l1  :
                if nums[l1]+nums[r]+nums[l]>0 :
                    r-=1
                elif nums[l1]+nums[r]+nums[l]<0:
                    l1+=1
                else :
                    res.append([nums[l],nums[l1],nums[r]])
                    l1+=1
                    r-=1
                    while r>l1 and nums[l1]==nums[l1-1] :
                        l1+=1

                    while r>l1 and nums[r]==nums[r+1] :
                        r-=1 


        return res


