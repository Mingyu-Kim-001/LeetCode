class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for _ in range(numRows):
            if not ans:
                ans.append([1])
            else:
                new_row = [1]
                for i in range(len(ans[-1])-1):
                    new_row.append(ans[-1][i]+ans[-1][i+1])
                new_row.append(1)
                ans.append(new_row)
        return ans