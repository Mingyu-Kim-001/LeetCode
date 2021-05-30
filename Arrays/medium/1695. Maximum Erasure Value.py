class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = r = ans = 0
        unique_window = set()
        unique_window_sum = 0
        while r < len(nums):
            while nums[r] in unique_window:
                unique_window.remove(nums[l])
                unique_window_sum -= nums[l]
                l += 1
            unique_window.add(nums[r])
            unique_window_sum += nums[r]
            ans = max(ans, unique_window_sum)
            r += 1
        return ans
            