from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count_at = defaultdict(int)
        for row in wall:
            prefix = 0
            for i,brick_width in enumerate(row):
                if i < len(row) - 1:
                    prefix += brick_width
                    edge_count_at[prefix] += 1
        return len(wall) - (max(edge_count_at.values()) if edge_count_at else 0)
                
                