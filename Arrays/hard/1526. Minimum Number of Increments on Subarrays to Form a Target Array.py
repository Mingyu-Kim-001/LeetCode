class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = prev = 0
        for num in target:
            ans += max(num - prev, 0)
            prev = num
        return ans