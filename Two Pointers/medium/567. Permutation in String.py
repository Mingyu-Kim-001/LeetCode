from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0
        s1count = Counter(s1)
        current_count = defaultdict(int)
        while r < len(s2):
            if s2[r] in s1count:
                while l < r and current_count[s2[r]] >= s1count[s2[r]]:
                    current_count[s2[l]] -= 1
                    l += 1
                current_count[s2[r]] += 1
            else:
                l = r + 1
                current_count = defaultdict(int)
            if r - l == len(s1) - 1:
                return True
            r += 1
        return False