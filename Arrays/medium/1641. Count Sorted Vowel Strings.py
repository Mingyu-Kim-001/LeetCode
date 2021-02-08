class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1]*5
        for i in range(1,n):
            dp2 = [0]*5
            dp2[0] = sum(dp)
            dp2[1] = sum(dp[1:])
            dp2[2] = sum(dp[2:])
            dp2[3] = sum(dp[3:])
            dp2[4] = sum(dp[4:])
            dp = dp2
        return sum(dp)