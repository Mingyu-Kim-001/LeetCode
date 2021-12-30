class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        remainder = 1
        ans = 1
        for _ in range(k+1):
            if remainder == 0:
                return ans
            remainder = (10 * remainder + 1) % k
            ans += 1
        return -1