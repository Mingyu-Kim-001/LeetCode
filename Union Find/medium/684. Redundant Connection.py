class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = float("-inf")
        for x,y in edges:
            N = max([x,y,N])
        root = list(range(N+1))
        rank = [1]*(N+1)
        def find(p):
            if root[p]!=p:
                root[p] = find(root[p])
            return root[p]
        def union(p,q):
            p1,q1 = find(p),find(q)
            if rank[p1]>rank[q1]:
                root[q1] = p1
                rank[p1]+=rank[q1]
            else:
                root[p1] = q1
                rank[q1]+=rank[p1]
        for p,q in edges:
            if find(p)!=find(q):
                union(p,q)
            else:
                return [p,q]