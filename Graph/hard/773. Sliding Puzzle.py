from collections import deque
class Solution:
    def slidingPuzzle(self, board) -> int:
        def swapElements(board,i,j):
            newboard = list(board)
            newboar[i],newboard[j] = newboard[j],newboard[i]
            return tuple(newboard)
        def isInBoard(i):
            return 0<=i<6
        moves = {0:[1,3],1:[-1,1,3],2:[-1,3],3:[-3,1],4:[-3,-1,1],5:[-1,-3]}
        isVisited = {}
        minNumOfMoves = float("inf")
        for i in range(2):
            for j in range(3):
                if board[i][j]==0:
                    zeroIndex = i*3+j
                    
        board = tuple(board[0]+board[1])
        bfs = deque([[board,zeroIndex,0]])
        isVisited[board]=True
        while bfs:
            board,zeroIndex,numOfMoves = bfs.popleft()
            if numOfMoves>=minNumOfMoves:continue
            if board==(1,2,3,4,5,0):
                minNumOfMoves = numOfMoves
                continue
            for move in moves[zeroIndex]:
                if isInBoard(zeroIndex+move):
                    newBoard = swapElements(board,zeroIndex,zeroIndex+move)
                    if not isVisited.get(newBoard,False):
                        isVisited[newBoard] = True
                        bfs.append([newBoard,zeroIndex+move,numOfMoves+1])
        return minNumOfMoves if minNumOfMoves!=float("inf") else -1