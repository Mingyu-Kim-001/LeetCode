class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(sum([1 for num in position if num % 2 == 0]), 
                   sum([1 for num in position if num % 2 == 1])
                  )