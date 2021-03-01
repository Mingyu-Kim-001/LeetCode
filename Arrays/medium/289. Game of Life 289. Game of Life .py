class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isInBoard(x,y):
            return 0<=x<m and 0<=y<n
        m,n = len(board),len(board[0])
        moves = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        neighbors = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                n_neighbor = 0
                for movei,movej in moves:
                    newi,newj = i+movei,j+movej
                    n_neighbor+=int(isInBoard(newi,newj) and board[newi][newj]==1)
                neighbors[i][j] = n_neighbor
        for i in range(m):
            for j in range(n):
                n_neighbor = neighbors[i][j]
                if board[i][j]:
                    if n_neighbor<2 or n_neighbor>3: board[i][j] = 0
                else:
                    if n_neighbor==3: board[i][j] = 1
        