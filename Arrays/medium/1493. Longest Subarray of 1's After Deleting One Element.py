class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = zeros = cur = ans = 0
        while l <= r < len(nums):
            if nums[r] == 0:
                zeros += 1
                while zeros > 1:
                    if nums[l]:
                        cur -= 1
                    else:
                        zeros -= 1
                    l += 1
            else:
                cur += 1
                ans = max(ans, cur)
            r += 1
        return ans if zeros else ans - 1