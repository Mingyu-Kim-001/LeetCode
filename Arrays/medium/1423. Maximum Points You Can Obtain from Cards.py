class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cur = ans = sum(cardPoints[:k])
        for i in range(k-1,-1,-1):
            cur = cur - cardPoints[i] + cardPoints[i-k]
            ans = max(ans,cur)
        return ans