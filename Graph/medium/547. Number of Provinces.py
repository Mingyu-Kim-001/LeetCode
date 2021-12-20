Time: O(n)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = [False]*n
        def DFS(x):
            visit[x] = True
            for y in range(n):
                if isConnected[x][y] and x!=y and not visit[y]:
                    DFS(y)
        result = 0
        for i in range(n):
            if not visit[i]:
                DFS(i)
                result+=1
        return result