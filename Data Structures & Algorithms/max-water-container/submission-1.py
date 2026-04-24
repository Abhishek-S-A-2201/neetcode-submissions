class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_container = 0
        l = 0
        r = len(heights)-1

        while l < r:
            print(heights[l], heights[r])
            area = (r-l)*min(heights[l], heights[r])
            max_container = max(max_container, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_container
        