#Time: O(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        mostWater = 0
        while l<r:
            mostWater = max(mostWater,min(height[r],height[l])*(r-l))
            if height[r]<height[l]: r-=1
            else: l+=1
        return mostWater