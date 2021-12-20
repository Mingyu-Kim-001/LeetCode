class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        isVisit = [False]*len(graph)
        result = []
        n = len(graph)
        def DFS(path,node):
            if node==n-1:
                result.append(path+[node])
                return
            isVisit[node] = True
            for neighbor in graph[node]:
                if not isVisit[neighbor]:
                    DFS(path+[node],neighbor)
            isVisit[node] = False
        DFS([],0)
        return result