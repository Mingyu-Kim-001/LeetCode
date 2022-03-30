class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or matrix[-1][-1] < target:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m - 1
        while l < r:
            m = (l + r + 1) // 2
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][0] < target:
                l = m
            else:
                return True
        row = l
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False