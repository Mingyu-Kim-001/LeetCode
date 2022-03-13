from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        prev, curr = 0, 0
        for num in range(max(counter.keys()) + 1):
            prev, curr = curr, max(curr, prev + num * counter[num])
        return max(prev, curr)