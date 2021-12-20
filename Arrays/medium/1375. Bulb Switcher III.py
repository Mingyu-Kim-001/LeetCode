class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        max_num = float("-inf")
        ans = 0
        for i,num in enumerate(light):
            max_num = max(max_num,num)
            if i + 1 == max_num:
                ans += 1
        return ans