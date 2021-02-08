class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        cIndex = []
        result = []
        for i,ch in enumerate(s):
            if ch==c:
                cIndex.append(i)
        prevIndex = -1
        for i in range(len(s)):
            if prevIndex==-1:
                result.append(cIndex[0]-i)
                if i==cIndex[0]:
                    prevIndex = 0
            elif prevIndex==len(cIndex)-1:
                result.append(i-cIndex[-1])
            else:
                result.append(min(i-cIndex[prevIndex],cIndex[prevIndex+1]-i))
                if i==cIndex[prevIndex+1]:
                    prevIndex+=1
        return result