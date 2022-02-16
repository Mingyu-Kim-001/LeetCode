class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        sort_by_start = sorted(events)
        sort_by_end = sorted(events, key = lambda x:x[1])
        heap = []
        idx = 0
        current_max_val = float("-inf")
        ans = 0
        for s, e, v in sort_by_start:
            while idx < len(events) and sort_by_end[idx][1] < s:
                current_max_val = max(current_max_val, sort_by_end[idx][2])
                idx += 1
            ans = max(ans, current_max_val + v, v)
        return ans