class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        children = [[] for _ in range(n + 1)]
        max_time = [0] * (n + 1)
        for parent, child in relations:
            children[parent].append(child)
        
        def DFS(node):
            if max_time[node] == 0: #first time visit
                for child in children[node]:
                    max_time[node] = max(max_time[node], DFS(child))
                max_time[node] += time[node - 1]
            return max_time[node]
            
        for node in range(1, n + 1):
            DFS(node)
        return max(max_time)
            