class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = l = r = 0
        zero_count = 0 
        while r < len(nums):
            zero_count += 1 - nums[r]
            while zero_count > k:
                zero_count -= 1 - nums[l]
                l += 1
            r += 1
            ans = max(ans, r - l)
        return ans