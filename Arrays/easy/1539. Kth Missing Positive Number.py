class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prev_positive = 0
        for i in arr:
            if i - prev_positive>1:
                if k > i - prev_positive - 1:
                    k-= i - prev_positive - 1
                else:
                    return prev_positive+k
            prev_positive = i
        return prev_positive+k