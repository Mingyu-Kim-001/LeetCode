class unionFind:
    def __init__(self,n):
        self.rank = [1]*n
        self.root = list(range(n))
    def find(self,p):
        if self.root[p]!=p:
            self.root[p] = self.find(self.root[p])
        return self.root[p]
    def union(self,p,q):
        rootp,rootq = self.find(p),self.find(q)
        if self.rank[rootp]>self.rank[rootq]:
            self.root[rootq] = rootp
            self.rank[rootp]+=self.rank[rootq]
        else:
            self.root[rootp] = rootq
            self.rank[rootq]+=self.rank[rootp]
            
            
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x:(x[2],x[0],x[1]))
        queries = [query+[i] for i,query in enumerate(queries)]
        queries.sort(key=lambda x:(x[2],x[0],x[1],x[2]))
        edgeIdx = 0
        uf = unionFind(n)
        result = [False]*len(queries)
        for p,q,limit,org_idx in queries:
            while edgeIdx<len(edgeList) and limit>edgeList[edgeIdx][2]:
                uf.union(edgeList[edgeIdx][0],edgeList[edgeIdx][1])
                edgeIdx+=1
            result[org_idx] = uf.find(p)==uf.find(q)
        return result