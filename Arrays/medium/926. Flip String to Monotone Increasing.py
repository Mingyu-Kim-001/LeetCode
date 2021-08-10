class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        front_1 = 0
        back_0 = sum([int(c == "0") for c in s])
        ans = front_1 + back_0
        for c in s:
            if c == "1":
                front_1 += 1
            else:
                back_0 -= 1
            ans = min(ans, back_0 + front_1)
        return ans
            