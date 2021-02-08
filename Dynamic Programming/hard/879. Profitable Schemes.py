from collections import defaultdict
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group, profit) -> int:
        MOD = pow(10,9) + 7
        dp = []
        for i in range(n+1):
            dp.append([0]*(minProfit+1))
        dp[0][0] = 1
        
        for g,p in zip(group,profit):
            # look = []
            # for i in range(n-g+1):
            #     for j in range(minProfit+1):
            #         if dp[i][j]!=0:
            #             look.append((i,j,dp[i][j]))
            for cur_g in range(n-g,-1,-1):
                for cur_p in range(minProfit,-1,-1):
                    dp[cur_g+g][min(cur_p+p,minProfit)]+=dp[cur_g][cur_p]
                

        result = 0
        for i in range(n+1):
            result+=dp[i][minProfit]
        return result%MOD