class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        n = len(dominoes)
        dist_from_right = [-1] * n
        dist_from_left = [-1] * n
        prev_right = float("-inf")
        prev_left = float("inf")
        ans = ""
        for i in range(n):
            if dominoes[i] == "R":
                prev_right = i
            elif dominoes[i] == "L":
                prev_right = float("-inf")
            dist_from_right[i] = (i - prev_right)
            
        for i in range(n-1, -1, -1):
            if dominoes[i] == "L":
                prev_left = i
            elif dominoes[i] == "R":
                prev_left = float("inf")
            dist_from_left[i] = prev_left - i
        
        for i in range(n):
            if dist_from_right[i] > dist_from_left[i]:
                ans += "L"
            elif dist_from_right[i] < dist_from_left[i]:
                ans += "R"
            else:
                ans += "."
        return ans
                  