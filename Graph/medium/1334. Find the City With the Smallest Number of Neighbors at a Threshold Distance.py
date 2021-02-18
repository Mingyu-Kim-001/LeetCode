#Time: O(n^3)
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dp = [[[float("inf")]*(n+1) for _ in range(n)] for _ in range(n)] #dp[i][j][k] means the minimum distance from i to j via cities of which index is less than k
        for i,j,d in edges:
            dp[i][j][0] = d
            dp[j][i][0] = d
        for k in range(1,n+1):
            for i in range(n):
                for j in range(n):
                    if i==j: 
                        dp[i][j][k] = 0
                    else:
                        dp[i][j][k] = min(dp[i][j][k-1],dp[i][k-1][k-1] + dp[k-1][j][k-1])
        minNeighbor = float("inf")
        result = 0
        for i in range(n):
            neighbor = 0
            for j in range(n):
                if i!=j and dp[i][j][k]<=distanceThreshold:
                    neighbor+=1
            if minNeighbor>=neighbor:
                minNeighbor = neighbor
                result = i
        return result