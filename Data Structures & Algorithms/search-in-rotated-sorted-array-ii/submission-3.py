class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l+(-l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        print(l)
        def search1 ( nums: List[int], target: int) :
            left=0
            right=len(nums)-1
            while left <right :
                mid= left+ (right-left)//2
                if nums[mid] >= target :
                    right=mid
                else :
                    left = mid+1
            return left if nums[left] ==target  else -1
        if pivot>0 :
            if search1(nums[:l],target)==-1 and search1(nums[l:],target) == -1 :
                    return False 
            else : 
                return True
        else : 
            if search1(nums,target)==-1 :
                return False 
            else :
                return True



        