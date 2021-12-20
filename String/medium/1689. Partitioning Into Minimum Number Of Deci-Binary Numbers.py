class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for c in n:
            ans = max(ans,int(c))
        return ans