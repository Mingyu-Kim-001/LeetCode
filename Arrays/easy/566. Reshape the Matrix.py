class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if r * c != m * n:
            return mat
        ans = []
        new_row = []
        for row in mat:
            for element in row:
                if len(new_row) < c:
                    new_row.append(element)
                else:
                    ans.append(new_row)
                    new_row = [element]
        if new_row:
            ans.append(new_row)
        return ans