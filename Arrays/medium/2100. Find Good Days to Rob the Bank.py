class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if not time:
            return list(range(len(security)))
        decreasing = [0] * len(security)
        increasing = [0] * len(security)
        ans = []
        for i in range(1, len(security)):
            decreasing[i] = 0 if security[i-1] < security[i] else decreasing[i-1] + 1
        for i in range(len(security) - 2, -1, -1):
            increasing[i] = 0 if security[i] > security[i+1] else increasing[i+1] + 1
        for i in range(len(security)):
            if decreasing[i] >= time and increasing[i] >= time:
                ans.append(i)
        return ans