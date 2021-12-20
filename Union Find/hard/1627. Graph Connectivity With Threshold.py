#Time: O(nlogn)
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        parent = list(range(n+1))#union-find
        rank = [1]*(n+1)
        def find(num):
            if parent[num]!=num:
                parent[num] = find(parent[num]) #path compression
                return parent[num]
            return num
        def union(num1,num2):
            n1 = find(num1)
            n2 = find(num2)
            if rank[n1]>rank[n2]:
                parent[n2] = n1
                rank[n1]+=rank[n2]
            else:
                parent[n1] = n2
                rank[n2]+=rank[n1]
        for divisor in range(threshold+1,n+1):
            if find(divisor)!=divisor: continue 
            num = divisor*2
            while num<=n:
                union(divisor,num)
                num+=divisor
        result = []
        for x,y in queries:
            result.append(find(x)==find(y))
        return result