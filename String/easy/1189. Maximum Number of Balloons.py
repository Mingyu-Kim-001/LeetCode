class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = dict()
        count["b"] = count["a"] = count["l"] = count["o"] = count["n"] = 0
        for c in text:
            if c in count:
                count[c] += 1
        return min(count["b"], count["a"], count["l"] // 2, count["o"] // 2, count["n"])