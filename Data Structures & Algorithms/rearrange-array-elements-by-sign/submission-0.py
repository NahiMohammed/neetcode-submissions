class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        posi = 0 
        neg = 1
        res =[0]*len(nums)
        for i in range(len(nums)) :
            if nums[i]>0 :
                res[posi] = nums[i]
                posi+=2
            else :
                res[neg] = nums[i]
                neg+=2
        return res