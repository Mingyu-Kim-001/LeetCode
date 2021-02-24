from collections import defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red_neighbors = defaultdict(list)
        blue_neighbors = defaultdict(list)
        red_pathLen = defaultdict(lambda: float("inf"))
        blue_pathLen = defaultdict(lambda: float("inf"))
        red_pathLen[0] = blue_pathLen[0] = 0
        for depart,dest in red_edges:
            red_neighbors[depart].append(dest)
        for depart,dest in blue_edges:
            blue_neighbors[depart].append(dest)
        def DFS(depart,col,pathLen):
            if col=="red":
                for neighbor in red_neighbors[depart]:
                    if red_pathLen[neighbor]>pathLen:
                        red_pathLen[neighbor] = pathLen
                        DFS(neighbor,"blue",pathLen+1)
            else:
                for neighbor in blue_neighbors[depart]:
                    if blue_pathLen[neighbor]>pathLen:
                        blue_pathLen[neighbor] = pathLen
                        DFS(neighbor,"red",pathLen+1)
        DFS(0,"red",1)
        DFS(0,"blue",1)
        result = []
        for i in range(n):
            minimumLen = min(red_pathLen[i],blue_pathLen[i])
            result.append(minimumLen if minimumLen!=float("inf") else -1)
        return result