class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small=[]
        big  = []
        for i in range(len(nums)) :
            if nums[i]<pivot :
                small.append(nums[i])
            elif nums[i]>pivot :
                big.append(nums[i])
        for i in range(len(small)) :
            nums[i] = small[i]
        for i in range(len(small),len(nums)-len(big)) :
            nums[i] = pivot
        for i in range(len(nums)-1 , len(nums)-len(big)-1,-1): 
            nums[i] = big[-len(nums)+i]

        return nums