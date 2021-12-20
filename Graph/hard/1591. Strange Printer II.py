from collections import defaultdict,deque
class Solution:
    def isPrintable(self, targetGrid) -> bool:
        def isSquare(colorNum):
            for i in range(upMost[colorNum],downMost[colorNum]+1):
                for j in range(leftMost[colorNum],rightMost[colorNum]+1):
                    if targetGrid[i][j]!=colorNum and targetGrid[i][j]!=-1:
                        return False
            return True
        
        def fillWithMinusOne(colorNum):
            for i in range(upMost[colorNum],downMost[colorNum]+1):
                for j in range(leftMost[colorNum],rightMost[colorNum]+1):
                    targetGrid[i][j] = -1
                    
        m = len(targetGrid)
        n = len(targetGrid[0])
        leftMost = defaultdict(lambda :100)
        rightMost = defaultdict(lambda :-1)
        upMost = defaultdict(lambda :100)
        downMost = defaultdict(lambda :-1)
        colorList = set()
        for i in range(m):
            for j in range(n):
                if leftMost[targetGrid[i][j]]>j: 
                    leftMost[targetGrid[i][j]]= j
                if rightMost[targetGrid[i][j]]<j: 
                    rightMost[targetGrid[i][j]]= j
                if upMost[targetGrid[i][j]]>i: 
                    upMost[targetGrid[i][j]] = i
                if downMost[targetGrid[i][j]]<i: 
                    downMost[targetGrid[i][j]] = i
                colorList.add(targetGrid[i][j])
        isChanged = True
        colorList = list(colorList)
        k = len(colorList)
        while isChanged:
            isChanged = False
            for i in range(k):
                if colorList[i]!=-1 and isSquare(colorList[i]):
                    fillWithMinusOne(colorList[i])
                    isChanged=True
                    colorList[i] = -1
            if sum(colorList) == -k:
                return True
        return False