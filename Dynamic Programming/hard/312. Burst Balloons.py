class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #add paddings to nums, and burst zero ballons in advance. 
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)
        
        #dp[i][j] : maximum score when ballon between ith and jth(excluding ith and jth)
        dp = [[0] * n for _ in range(n)]
        
        for step in range(2, n):
            for i in range(n - step):
                j = i + step
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        return dp[0][-1]
        