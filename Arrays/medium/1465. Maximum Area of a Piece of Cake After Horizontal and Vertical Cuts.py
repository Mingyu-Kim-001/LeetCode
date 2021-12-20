class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        height_max = width_max = 0
        prev_horizontal_cut = prev_vertical_cut = 0
        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        for horizontal_cut in horizontalCuts:
            height_max = max(height_max, horizontal_cut-prev_horizontal_cut)
            prev_horizontal_cut = horizontal_cut
            
        for vertical_cut in verticalCuts:
            width_max = max(width_max, vertical_cut-prev_vertical_cut)
            prev_vertical_cut = vertical_cut
        
        return (height_max * width_max) % (pow(10,9) + 7)