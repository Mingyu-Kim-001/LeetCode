class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        stack = []
        for i,num in enumerate(T):
            while stack and T[stack[-1]] < num:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result