class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0])
        n = len(costs) // 2
        return sum([costs[i][1] for i in range(n)]) + sum([costs[i][0] for i in range(n, 2*n)])