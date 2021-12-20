class Solution:
    def numDecodings(self, s: str) -> int:
        valid_encoding = set([str(i) for i in range(1,27)])
        dp = [0] * (len(s)+1)
        dp[0] = 1
        for i in range(1,len(s)+1):
            dp[i] = (dp[i-1] if i - 1 >= 0 and s[i-1] in valid_encoding else 0) + (dp[i-2] if i - 2 >= 0 and s[i-2:i] in valid_encoding else 0)
        return dp[len(s)]