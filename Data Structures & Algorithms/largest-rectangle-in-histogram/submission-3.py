class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftmost = [-1]* n
        stack = []
        for i in range(n) : 
            while stack and heights[stack[-1]]>=heights[i] :
                stack.pop()
            if stack :
                leftmost[i] = stack[-1]
            stack.append(i)
        rightmost = [n]*n
        stack= []
        for i in range(n-1,-1,-1) : 
            while stack and heights[stack[-1]]>=heights[i] :
                stack.pop()
            if stack :
                rightmost[i] = stack[-1]
            stack.append(i)

        res = 0 
        for i in range(n):
            leftmost[i] += 1
            rightmost[i] -= 1
            res = max(res, heights[i] * (rightmost[i] - leftmost[i] + 1))
        return res
        