class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrows = 0
        currEnd = None
        for x,y in points:
            if not currEnd or x>currEnd:
                currEnd = y
                arrows+=1
        return arrows