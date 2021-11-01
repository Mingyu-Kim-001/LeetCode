from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        window = deque()
        increasing = deque()
        decreasing = deque()
        ans = 0
        for i,num in enumerate(nums):
            while increasing and num - increasing[0][1] > limit:
                cur_min_idx, cur_min = increasing.popleft()
                while decreasing and decreasing[0][0] <= cur_min_idx:
                    decreasing.popleft()
                while window and window[0][0] <= cur_min_idx:
                    window.popleft()

            while decreasing and decreasing[0][1] - num > limit:
                cur_max_idx, cur_max = decreasing.popleft()
                while increasing and increasing[0][0] <= cur_max_idx:
                    increasing.popleft()
                while window and window[0][0] <= cur_max_idx:
                    window.popleft()
            window.append([i, num])
            while increasing and increasing[-1][1] >= num:
                increasing.pop()
            increasing.append([i, num])
            while decreasing and decreasing[-1][1] <= num:
                decreasing.pop()
            decreasing.append([i, num])
                        
            ans = max(ans, len(window))
        
        return ans
                    