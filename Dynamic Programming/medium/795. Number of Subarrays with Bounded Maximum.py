class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        nearest_gt_right = -1 # the index of leftmost num which is greater than right
        nearest_ge_left_count = 0 
        ans = 0
        for i, num in enumerate(nums):
            if num > right:
                nearest_gt_right = i
                nearest_ge_left_count = 0
            elif num < left:
                ans += nearest_ge_left_count
            else:
                ans += i - nearest_gt_right
                nearest_ge_left_count = i - nearest_gt_right
            
            
        return ans