class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        prev_prev_max = float("-inf")
        for i,a in enumerate(A):
            if i > 1:
                prev_prev_max = max(prev_prev_max,A[i-2])
            if a < prev_prev_max:
                return False
        return True
                