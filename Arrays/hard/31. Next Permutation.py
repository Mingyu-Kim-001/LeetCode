#Time: O(n)
class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        MOD = pow(10,9) + 7
        pow2 = []
        prev = 1
        for i in range(len(A)):
            pow2.append(prev)
            prev = (prev*2)%MOD
        n = len(A)
        A.sort()
        result = 0
        for i,num in enumerate(A):
            result+=(pow2[i]*num - pow2[len(A)-1-i]*num)%MOD
        return result%MOD