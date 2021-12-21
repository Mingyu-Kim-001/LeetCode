class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        ans = [0] * len(heights)
        mono_dec = []
        for i, height in enumerate(heights):
            while mono_dec and mono_dec[-1][0] < height:
                _, idx = mono_dec.pop()
                ans[idx] += 1
            if mono_dec:
                ans[mono_dec[-1][1]] += 1
            mono_dec.append([height,i])
        return ans