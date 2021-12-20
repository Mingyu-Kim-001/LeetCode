#Time:O(ink)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        def isInBoard(i,j):
            return 0<=i<m and 0<=j<n
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        def DFS(word,wordIndex,x,y):
            if word[wordIndex]!=board[x][y]: return False
            if wordIndex==len(word)-1:return True
            store = board[x][y]
            board[x][y] = ""
            
            for movex,movey in moves:
                newx,newy = x+movex, y+movey
                if isInBoard(newx,newy) and DFS(word,wordIndex+1,newx,newy):
                    board[x][y] = store
                    return True
            
            board[x][y] = store
            return False
        result = []
        for word in words:
            xyGrid = [[i,j] for i in range(m) for j in range(n)]
            for x,y in xyGrid:
                if DFS(word,0,x,y):
                    result.append(word)
                    break
        return result