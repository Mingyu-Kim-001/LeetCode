class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
        dp = [False] * (half+1)
        dp[0] = True
        for num in nums:
            for i in range(half,-1,-1):
                if not dp[i] and i - num >=0 and dp[i-num]:
                    dp[i] = True
        return dp[half]
        