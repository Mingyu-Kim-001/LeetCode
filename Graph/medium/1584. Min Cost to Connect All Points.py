#Time: O(n^2)
import heapq as hq
class Solution:
    def minCostConnectPoints(self, points) -> int:
        def dist(p1,p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n = len(points)
        neighbors = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i!=j:neighbors[i].append((dist(points[i],points[j]),j))
        visit = [False]*n
        visit[0] = True
        result = 0
        heap = neighbors[0]
        hq.heapify(heap)
        count = 1
        while heap:
            distance,j = hq.heappop(heap)
            if not visit[j]:
                visit[j] = True
                result+=distance
                count+=1
                if count==n: return result
                for neighbor in neighbors[j]:
                    if not visit[neighbor[1]]:hq.heappush(heap,neighbor)
        return result