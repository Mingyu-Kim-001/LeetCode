class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 1:
            return (n+1) * (n-1) // 4
        else:
            return n * n // 4