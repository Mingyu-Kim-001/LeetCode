class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:return 0
        result = [0,1]
        maxvalue = 1
        for i in range(2,n+1):
            if i%2==0:
                nextelement = result[i//2]
                maxvalue = max(maxvalue,nextelement)
                result.append(nextelement)
            else:
                nextelement = result[i//2] + result[i//2+1]
                maxvalue = max(maxvalue,nextelement)
                result.append(nextelement)
        return maxvalue
                