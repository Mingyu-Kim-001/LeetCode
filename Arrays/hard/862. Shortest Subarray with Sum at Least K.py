from collections import deque
#Time:O(n)
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        monotoneIncreasing = deque([[0,0]])
        result = float("inf")
        prefix = 0
        for i,num in enumerate(A):
            prefix+=num
            while monotoneIncreasing and monotoneIncreasing[-1][1]>=prefix:
                monotoneIncreasing.pop()
            monotoneIncreasing.append([i+1,prefix])
            while monotoneIncreasing and i-monotoneIncreasing[0][0]>=result:
                monotoneIncreasing.popleft()
            while monotoneIncreasing and prefix - monotoneIncreasing[0][1]>=K:
                result = i+1-monotoneIncreasing.popleft()[0]
        return result if result!=float("inf") else -1