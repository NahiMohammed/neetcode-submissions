class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        counts = {}
        answer = 0
        for width, height in rectangles:

            key = height/width
            answer += counts.get(key, 0)
            counts[key] = counts.get(key, 0) + 1
        return answer