from collections import Counter
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if all(A[0] in i for i in zip(A,B)): 
            return min(len(A)-A.count(A[0]),len(B)-B.count(A[0]))
        if all(B[0] in i for i in zip(A,B)):
            return min(len(A)-A.count(B[0]),len(B)-B.count(B[0]))
        return -1