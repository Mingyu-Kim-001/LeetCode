#Time: O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = []
        right = []
        midLeft = newInterval[0]
        midRight = newInterval[1]
        for interval in intervals:
            if interval[1]<newInterval[0]:
                left.append(interval)
            elif interval[0]>newInterval[1]:
                right.append(interval)
            else:
                midLeft = min(midLeft,interval[0])
                midRight = max(midRight,interval[1])
        return left+[[midLeft,midRight]]+right