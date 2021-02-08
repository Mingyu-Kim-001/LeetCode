from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        diagonal = defaultdict(list)
        
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                diagonal[i-j].append(mat[i][j])
        for i in diagonal:
            diagonal[i].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonal[i-j].pop()
        return mat
        
            