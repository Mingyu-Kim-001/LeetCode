from collections import defaultdict
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m,n = len(targetGrid),len(targetGrid[0])
        colors = set()
        for i in targetGrid:
            colors = colors | set(i)
        leftMost = defaultdict(lambda:float("inf"))
        rightMost = defaultdict(lambda:float("-inf"))
        upMost = defaultdict(lambda:float("inf"))
        downMost = defaultdict(lambda:float("-inf"))
        for i in range(m):
            for j in range(n):
                leftMost[targetGrid[i][j]] = min(leftMost[targetGrid[i][j]],j)
                rightMost[targetGrid[i][j]] = max(rightMost[targetGrid[i][j]],j)
                upMost[targetGrid[i][j]] = min(upMost[targetGrid[i][j]],i)
                downMost[targetGrid[i][j]] = max(downMost[targetGrid[i][j]],i)
        def isPaintable(color):
            for i in range(upMost[color],downMost[color]+1):
                for j in range(leftMost[color],rightMost[color]+1):
                    if targetGrid[i][j]!=-1 and targetGrid[i][j]!=color:
                        return False
            for i in range(upMost[color],downMost[color]+1):
                for j in range(leftMost[color],rightMost[color]+1):
                    targetGrid[i][j] = -1
            return True
        while colors:
            for color in list(colors):
                if isPaintable(color):
                    colors.remove(color)
                    break
            else:
                return False
        return True