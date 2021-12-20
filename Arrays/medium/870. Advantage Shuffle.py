#Time: O(blogs)
from collections import deque
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        B_sort = sorted([[i,b] for i,b in enumerate(B)],key=lambda x:-x[1])
        result = [None] * len(A)
        A = deque(sorted(A))
        for i,b in B_sort:
            if A[-1] > b:
                result[i] = A.pop()
            else:
                result[i] = A.popleft()
        return result