#Time: O(mn)
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]: return []
        m = len(matrix)
        n = len(matrix[0])
        pVisit = [[False]*n for _ in range(m)]
        aVisit = [[False]*n for _ in range(m)]
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        def isInBoard(x,y):
            return 0<=x<m and 0<=y<n
        def DFS(x,y,visit):
            if visit[x][y]:return
            visit[x][y] = True
            for movex,movey in moves:
                newx,newy = x+movex,y+movey
                if isInBoard(newx,newy) and not visit[newx][newy] and matrix[newx][newy]>=matrix[x][y]:
                    DFS(newx,newy,visit)
        for x in range(m):
            DFS(x,0,pVisit)
            DFS(x,n-1,aVisit)
        for y in range(n):
            DFS(0,y,pVisit)
            DFS(m-1,y,aVisit)
        result = []
        for x in range(m):
            for y in range(n):
                if pVisit[x][y] and aVisit[x][y]:
                    result.append([x,y])
        return result