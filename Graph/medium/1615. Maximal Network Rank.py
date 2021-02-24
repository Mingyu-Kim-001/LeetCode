#Time: O(n^2)
from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        neighbors = defaultdict(set)
        for x,y in roads:
            neighbors[x].add(y)
            neighbors[y].add(x)
        result = float("-inf")
        for i in range(n):
            for j in range(i+1,n):
                result = max(result,len(neighbors[i])+len(neighbors[j])-(1 if j in neighbors[i] else 0))
        return result