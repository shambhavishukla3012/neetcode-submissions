class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAr = 0

        l, r = 0, len(heights)-1
        while l<r:
            area = (r-l) * min(heights[l], heights[r])
            maxAr = max(maxAr,area)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return maxAr