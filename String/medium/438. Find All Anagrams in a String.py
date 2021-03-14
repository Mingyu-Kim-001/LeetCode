from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        diff = defaultdict(int)
        for c in p:
            diff[c] += 1
        for c in s[:len(p)]:
            if c in diff:
                diff[c] -= 1
        num_of_zeros = 0
        for val in diff.values():
            if not val:
                num_of_zeros += 1
        if num_of_zeros == len(diff):
            result.append(0)
        start = 1
        while start <= len(s) - len(p):
            end = start + len(p) - 1
            if s[end] in diff:
                diff[s[end]] -= 1
                if diff[s[end]] == 0:
                    num_of_zeros += 1
                elif diff[s[end]] == -1:
                    num_of_zeros -= 1
            if s[start-1] in diff:
                diff[s[start-1]] += 1
                if diff[s[start-1]] == 0:
                    num_of_zeros += 1
                elif diff[s[start-1]] == 1:
                    num_of_zeros -= 1
            if num_of_zeros == len(diff):
                result.append(start)
            start += 1
        return result