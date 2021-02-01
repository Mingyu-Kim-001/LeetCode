# Time: O(n), Space: O(n)
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        visit = defaultdict(int)
        def DFS(num):
            if visit[num] or not num in numSet:
                return 0
            visit[num] = True
            return DFS(num-1) + 1 + DFS(num+1)
        result = 0
        for num in nums:
            if not visit[num]:
                result = max(result,DFS(num))
        return result