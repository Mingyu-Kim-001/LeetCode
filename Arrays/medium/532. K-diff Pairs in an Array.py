from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        ans = 0
        for num in counts:
            if (k + num in counts and k > 0) or (counts[num] > 1 and k == 0):
                ans += 1
        return ans