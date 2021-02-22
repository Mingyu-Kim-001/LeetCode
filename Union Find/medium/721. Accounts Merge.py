from collections import defaultdict
class unionFind:
    def __init__(self,n):
        self.root = list(range(n))
        self.rank = [1]*n
    def find(self,x):
        if self.root[x]!=x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self,x,y):
        x1,y1 = self.find(x),self.find(y)
        if self.rank[x1]>self.rank[y1]:
            self.root[y1] = x1
            self.rank[y1]+=self.rank[x1]
        else:
            self.root[x1] = y1
            self.rank[x1]+=self.rank[y1]
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = unionFind(n)
        names = []
        email_to_idx = {}
        for i,emails in enumerate(accounts):
            names.append(emails[0])
            for email in emails[1:]:
                if email in email_to_idx:
                    uf.union(email_to_idx[email],i)
                else:
                    email_to_idx[email] = i
        result = defaultdict(list)
        for email in email_to_idx:
            result[uf.find(email_to_idx[email])].append(email)
        for i in result:
            result[i] = [names[i]] + sorted(result[i])
        return [result[i] for i in result]