#Time: O(mn)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        isO = [[False]*n for _ in range(m)]
        def isInBoard(x,y):
            return 0<=x<m and 0<=y<n
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        def DFS(x,y):
            isO[x][y] = True
            for movex, movey in moves:
                newx,newy = x+movex,y+movey
                if isInBoard(newx,newy) and board[newx][newy]=="O" and not isO[newx][newy]:
                    DFS(newx,newy)
        for x in range(m):
            for y in range(n):
                if x==0 or x==m-1 or y==0 or y==n-1:
                    if board[x][y]=="O" and not isO[x][y]:
                        DFS(x,y)
        for x in range(m):
            for y in range(n):
                if isO[x][y]:
                    board[x][y] = "O"
                else:
                    board[x][y] = "X"
                    
                