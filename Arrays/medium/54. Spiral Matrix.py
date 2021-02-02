class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        m = len(matrix)
        n = len(matrix[0])
        if m==0 or n==0:return []
        
        count = 0
        result = []
        x,y=0,-1
        def isInMatrix(x,y):
            return 0<=x<m and 0<=y<n
        moves = [[0,1],[1,0],[0,-1],[-1,0]]
        while count<m*n:
            for movex, movey in moves:
                while True:
                    newx = x+movex
                    newy = y+movey
                    if isInMatrix(newx,newy) and matrix[newx][newy]!=-1000:
                        result.append(matrix[newx][newy])
                        matrix[newx][newy] = -1000
                        x,y=newx,newy
                        newx = x+movex
                        newy = y+movey
                        count+=1
                    else:
                        break

        return result