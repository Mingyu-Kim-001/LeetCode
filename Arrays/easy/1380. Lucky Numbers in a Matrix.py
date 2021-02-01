#Time: O(mn)
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0: return 0
        rowMin = []
        for row in matrix:
            rowMin.append(min(row))
        colMax = []
        for i in range(len(matrix[0])):
            colMax.append(max([row[i] for row in matrix]))
        return list(set(rowMin).intersection(colMax)) # This can be done because all the elements in the matrix are distinct