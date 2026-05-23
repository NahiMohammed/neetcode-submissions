class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n =len(heights)
        res=0
        
        for i in range(n):
            m=heights[i]
            if m==0 :
                continue
            for j in range(i,n):
                m=min(m,heights[j])
                res=max(res,m*(j-i+1))
        return res


        