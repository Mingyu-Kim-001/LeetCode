from collections import deque
from collections import defaultdict
class Node:
    def __init__(self,name):
        self.name = name
        self.edges = {}
    def addEdge(self,name,weight):
        self.edges[name] = weight
    
class Solution:
    def calcEquation(self, equations, values, queries):
        nodeDic = {}
        for eq,v in zip(equations,values):
            
            if not eq[0] in nodeDic:
                nodeDic[eq[0]] = Node(eq[0])
            nodeDic[eq[0]].addEdge(eq[1],v)
            
            if not eq[1] in nodeDic:
                nodeDic[eq[1]] = Node(eq[1])
            nodeDic[eq[1]].addEdge(eq[0],1/v)
            
        result = []
#         for k,v in nodeDic.items():
#             print(k,v)
        for q in queries:
            if not q[0] in nodeDic or not q[1] in nodeDic:
                result.append(-1)
                continue
            if q[0]==q[1]:
                result.append(1)
                continue
            dq = deque([[q[0],1]])
            isVisited = defaultdict(bool)
            while dq:
                name,product = dq.popleft()
                if name==q[1]:
                    result.append(product)
                    break
                for neighbor,weight in nodeDic[name].edges.items():
                    if not isVisited[neighbor]:
                        dq.append([neighbor,product*weight])
                        isVisited[neighbor] = True
            else:
                result.append(-1)
        return result