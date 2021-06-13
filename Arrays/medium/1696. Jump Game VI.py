from collections import deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        monotonic_decreasing = deque()
        
        for i, num in enumerate(nums):
            if monotonic_decreasing and monotonic_decreasing[0][1] < i - k:
                monotonic_decreasing.popleft()
            score = monotonic_decreasing[0][0] + num if i > 0 else num
            while monotonic_decreasing and monotonic_decreasing[-1][0] <= score:
                monotonic_decreasing.pop()
            monotonic_decreasing.append([score,i])
            
        return monotonic_decreasing[-1][0]
        