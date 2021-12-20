#Time: worst case O(mnk), where k is length of word
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wordLen = len(word)
        m = len(board)
        n = len(board[0])
        def isInBoard(x,y):
            return 0<=x<m and 0<=y<n
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        def DFS(x,y,wordIndex):
            if board[x][y]!=word[wordIndex]: return False
            if wordIndex==wordLen-1: return True
            org = board[x][y]
            board[x][y] = ""
            for movex,movey in moves:
                newx,newy = x+movex,y+movey
                if isInBoard(newx,newy) and DFS(newx,newy,wordIndex+1): return True
            board[x][y] = org
            return False
        for x in range(m):
            for y in range(n):
                if DFS(x,y,0): return True
        return False