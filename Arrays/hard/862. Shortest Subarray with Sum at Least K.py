from collections import deque
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        increasingDeque = deque([[0,-1]])
        minLen = float("inf")
        prefixSum = 0
        for i,num in enumerate(A):
            prefixSum+=num
            while increasingDeque and increasingDeque[-1][0]>=prefixSum:
                increasingDeque.pop()
            increasingDeque.append([prefixSum,i])
            while increasingDeque and i-increasingDeque[0][1]>=minLen:
                increasingDeque.popleft()
            while prefixSum - increasingDeque[0][0]>=K:
                minLen = i-increasingDeque.popleft()[1]
        return minLen if minLen!=float("inf") else -1