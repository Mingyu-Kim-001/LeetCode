class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        min_val = [0] * n
        for row_num,row in enumerate(triangle):
            min_val2 = [0] * row_num + [float("inf")] * (n-row_num)
            for i,num in enumerate(row):
                min_val2[i] = min(min_val[max(i-1,0)]+num,min_val[i]+num)
            min_val = min_val2
        return min(min_val)