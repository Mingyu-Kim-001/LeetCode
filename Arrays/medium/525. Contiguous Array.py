class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        stack = ans = 0
        seen = {}
        seen[0] = -1
        for i, num in enumerate(nums):
            stack += -1 if num else 1
            if stack in seen:
                ans = max(ans, i - seen[stack])
            else:
                seen[stack] = i
        return ans