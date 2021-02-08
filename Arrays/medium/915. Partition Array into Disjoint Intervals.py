class Solution:
    def partitionDisjoint(self, A) -> int:
        maxList = [A[0]]
        for i in A[1:]:
            maxList.append(max(maxList[-1],i))
        minList = [A[-1]]
        for i in A[-2::-1]:
            minList.append(min(minList[-1],i))
        
        n = len(A)
        #print(maxList,minList)
        for i in range(n):
            if maxList[i]<=minList[n-i-2]:
                return i+1