from collections import defaultdict
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        double_candidate = defaultdict(int)
        arr.sort(key=lambda x:abs(x))
        for num in arr:
            if not double_candidate[num]:
                double_candidate[num*2] += 1
            else:
                double_candidate[num] -= 1
        if sum(double_candidate.values()):
            return False
        return True