class Solution:
    def first_and_second(self, nums):
        first = second = float("inf")
        for idx, num in enumerate(nums):
            if first >= num:
                second = first
                first = num
            elif second > num:
                second = num
        return first, second
    
        
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]
        if n == 2:
            return min(grid[0][0] + grid[1][1], grid[1][0] + grid[0][1])
        dp = grid[0]
        for row_idx in range(1, n):
            first, second = self.first_and_second(dp)
            dp2 = [0] * n
            for col_idx in range(n):
                dp2[col_idx] = grid[row_idx][col_idx] + (second if dp[col_idx] == first else first)
            dp = dp2
        return min(dp)
        