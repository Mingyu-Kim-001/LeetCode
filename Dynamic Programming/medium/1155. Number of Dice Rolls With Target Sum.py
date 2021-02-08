from collections import defaultdict
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if f*d<target: return 0
        MOD = pow(10,9)+7
        dp = defaultdict(int)
        for j in range(1,f+1):
            dp[j] = 1
        for _ in range(d-1):
            #dp2 = defaultdict(int)
            for i in range(target,0,-1):
                dp[i]=0
                for j in range(1,f+1):
                    dp[i]+=dp[i-j]
                    #dp[i]%=MOD
            #dp = dp2
        return dp[target]%MOD