class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        lEnd = 0
        lMax = curMax = A[0]
        i = 1
        while i+1<len(A):
            curMax = max(curMax,A[i])
            if A[i]<lMax:
                lMax = curMax
                lEnd = i
            i+=1
        return lEnd+1