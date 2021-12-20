class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci_ = [0,1,1]
        while len(tribonacci_) <= n:
            tribonacci_.append(tribonacci_[-3] + tribonacci_[-2] + tribonacci_[-1])
        return tribonacci_[n]