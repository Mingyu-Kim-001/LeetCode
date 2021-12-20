class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_prev_cost = prev_cost = 0
        for i, cost in enumerate(cost):
            prev_cost, prev_prev_cost = min(prev_cost + cost if i > 0 else cost,prev_prev_cost + cost if i > 1 else cost), prev_cost
        
        return min(prev_cost,prev_prev_cost)