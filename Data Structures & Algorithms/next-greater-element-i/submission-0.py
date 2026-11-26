class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index={}
        for i , n in enumerate(nums2) :
            index[n] = i 
        result = {}          
        stack = []

        for x in nums2:
            while stack and x > stack[-1]:
                result[stack.pop()] = x
            stack.append(x)

        for x in stack:      
            result[x] = -1

        res = []
        for i , n in enumerate(nums1) :
            res.append(result[nums2[index[n]]])
        return res
        
        