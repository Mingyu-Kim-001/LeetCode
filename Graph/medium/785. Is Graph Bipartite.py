class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        node_set = set(range(len(graph)))
        visit = [False]*len(graph)
        def DFS(node,setIndex):
            visit[node] = True
            setList[setIndex].add(node)
            for neighbor in graph[node]:
                if neighbor in setList[setIndex]: return False
                if not visit[neighbor] and not DFS(neighbor,(setIndex+1)%2): return False
            return True
        for node in range(len(graph)):
            setList = [set(),set()]
            if not visit[node] and not DFS(node,0):
                return False
        return True