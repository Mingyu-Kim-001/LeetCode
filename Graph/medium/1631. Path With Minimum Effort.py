import heapq as hq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        def isInBoard(x,y):
            return 0<=x<m and 0<=y<n
        
        heap = [(0,0,0)]
        dist = [[float("inf")]*n for _ in range(m)]
        prev = [[None]*n for _ in range(m)]
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        dist[0][0] = 0
        while heap:
            d,x,y = hq.heappop(heap)
            # print(d,x,y)
            for movex,movey in moves:
                newx = x+movex
                newy = y+movey
                if isInBoard(newx,newy):
                    
                    newDist = min(max(abs(heights[newx][newy] - heights[x][y]),dist[x][y]),
                                   dist[newx][newy] )
                    # print(newx,newy,newDist)
                    if newDist<dist[newx][newy]:
                        dist[newx][newy] = newDist
                        hq.heappush(heap,(dist[newx][newy],newx,newy))
        # print(dist)              
        return dist[m-1][n-1]