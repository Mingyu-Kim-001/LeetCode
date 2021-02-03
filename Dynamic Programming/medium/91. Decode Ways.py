#Time: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1) # dp[i]: answer with s[:i]
        dp[0] = 1
        for i,c in enumerate(s):
            if i>0 and 10<=int(s[i-1:i+1])<=26:
                dp[i+1]+=dp[i-1]
            if 1<=int(s[i])<=9:
                dp[i+1]+=dp[i]
        return dp[len(s)]