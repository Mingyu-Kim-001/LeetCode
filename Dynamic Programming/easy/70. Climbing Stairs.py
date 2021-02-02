#Time: O(n), extra space: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        res = 1
        for i in range(1,n+1):
            temp = res
            res+=prev
            prev = temp
        return res