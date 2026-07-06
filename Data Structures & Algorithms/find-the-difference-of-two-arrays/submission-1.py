class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l0=[]
        l1=[]
        for i in set(nums1): 
            if i not  in nums2:
                l0.append(i)
        for i in set(nums2): 
            if i not  in nums1:
                l1.append(i)
        return [l0,l1]
        