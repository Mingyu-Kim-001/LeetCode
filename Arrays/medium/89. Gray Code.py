class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0,1]
        for i in range(n-1):
            power = pow(2, i + 1)
            for j in range(len(ans)-1,-1,-1):
                ans.append(ans[j] + power)
        return ans