class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        copie=heights.copy()
        heights.sort()

        res=0
        for i in range(len(heights)) :
            if heights[i]!=copie[i]:
                res+=1
        return res
        