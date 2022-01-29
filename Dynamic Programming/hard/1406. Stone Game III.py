class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        start_with = [0] * (n + 1) # start_with[i] = the maximum score gain(diff) when someone starts with index i (from zero base score)
        for i in range(n - 1, -1, -1):
            start_with[i] = max([sum(stoneValue[i:j]) - start_with[j] for j in range(i + 1, min(i + 4, n + 1))])
        return "Alice" if start_with[0] > 0 else ("Bob" if start_with[0] < 0 else "Tie")