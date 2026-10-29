class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0
        leftMax= [0]*n
        rightMax = [0]*n
        for i in range(1,n) :
            leftMax[i] = max(leftMax[i-1],height[i-1])
        for i in range(n-2,-1,-1) :
            rightMax[i] = max(rightMax[i+1],height[i+1])

        for i in range(1 , n-1 ) :
            if min(leftMax[i], rightMax[i])>height[i] :
                res+=min(leftMax[i], rightMax[i])-height[i]
        return res

"""
0 0 2 2 3 3 3 3 3 3
    2 0 2 3 2 0 0     
3 3 3 3 3 3 3 2 1 0 
"""