#Time: O(n)
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque([])
        windowLen = 0
        result = []
        for i,num in enumerate(nums):
            while window and window[-1][0]<num:
                window.pop()
            window.append([num,i])
            if window and i>=k and window[0][1]<=i-k:
                window.popleft()
            if i>=k-1:
                result.append(window[0][0])
        return result