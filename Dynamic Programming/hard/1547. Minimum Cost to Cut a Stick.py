from collections import defaultdict
class Solution:
    def minCost(self, n: int, cuts) -> int:
        cuts.sort()
        stickLength = [cuts[0]]
        for i in range(len(cuts)-1):
            stickLength.append(cuts[i+1]-cuts[i])
        stickLength.append(n-cuts[-1])
        prefixSum = [0]
        for i in stickLength:
            prefixSum.append(prefixSum[-1]+i)
        #print(stickLength)
        dp = defaultdict(int)
        for i in range(1,len(stickLength)):
            for j in range(len(stickLength)-i):
                dp[(j,j+i)] = min([dp[(j,j+x)] + dp[(j+x+1,j+i)] for x in range(i)]) + prefixSum[j+i+1] - prefixSum[j]
                #print(dp)
        return dp[(0,len(stickLength)-1)]