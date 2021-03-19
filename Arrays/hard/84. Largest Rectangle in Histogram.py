class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        result = 0
        for i,height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                j = stack[-1] if stack else -1
                result = max(result,h*(i-j-1))
            stack.append(i)
        while stack:
            h = heights[stack.pop()]
            j = stack[-1] if stack else -1
            result = max(result,h*(i-j))
        return result