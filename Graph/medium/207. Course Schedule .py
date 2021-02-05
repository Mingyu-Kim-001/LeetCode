#Time: O(n)
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        require = defaultdict(list)
        for i,j in prerequisites:
            require[i].append(j)
        visit = [0]*numCourses
        visitCount = 0
        def DFS(i):
            visit[i] = -1 #-1 means visiting in the cycle. 
            for j in require[i]:
                if visit[j]==-1:
                    return False
                elif visit[j]==0 and not DFS(j):
                    return False
            visit[i] = 1 # 1 means visiting is over
            return True
        for i in range(numCourses):
            if visit[i]==0 and not DFS(i):return False
        return True
            