#Time: O(nlogn)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        start = end = -1
        result = []
        for i,interval in enumerate(intervals):
            if start==-1:
                start,end = interval
            elif end<interval[0]:
                result.append([start,end])
                start,end = interval
            else:
                end = max(end,interval[1])
        result.append([start,end])
        return result