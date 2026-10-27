class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx_replacemnt = 0 
        i = 0 
        while i<len(nums) : 
            j = i+1
            number = nums[i]
            while j<len(nums) and nums[j]==nums[i] :
                j+=1
            for l in range(min(j-i , 2 )) :
                nums[idx_replacemnt] = number
                idx_replacemnt+=1
            i = j 
        return idx_replacemnt
