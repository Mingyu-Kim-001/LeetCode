class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        prev_2 = 0
        prev = 1
        ans = 1
        for _ in range(n-2):
            prev_2, prev, ans = prev, ans, ans + prev
        return ans