class Solution:
    def trap(self, height: List[int]) -> int:
        monotone_decreasing = []
        ans = 0
        for i, h in enumerate(height):
            prev = 0
            while monotone_decreasing and monotone_decreasing[-1][1] <= h:
                left_idx, left_height = monotone_decreasing.pop()
                ans += (i - left_idx - 1) * (left_height - prev)
                prev = left_height
            if monotone_decreasing:
                ans += (i - monotone_decreasing[-1][0] - 1) * (h - prev)
            monotone_decreasing.append([i, h])
        return ans