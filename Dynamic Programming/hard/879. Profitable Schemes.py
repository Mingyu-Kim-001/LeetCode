#Time: O(n)
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = pow(10,9) + 7
        dp = [[0]*(minProfit+1) for _ in range(n+1)] # dp[i][j] means the number of schemes with i members that generates min(j,minProfit) profits. 
        dp[0][0] = 1
        for n_member,p in zip(group,profit):
            for i in range(n,-1,-1):
                for j in range(minProfit,-1,-1):
                    if i+n_member<=n:
                        dp[i+n_member][min(j+p,minProfit)]+=dp[i][j]
                        dp[i+n_member][min(j+p,minProfit)]%=MOD
        return sum([dp[i][minProfit] for i in range(n+1)])%MOD