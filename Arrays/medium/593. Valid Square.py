from itertools import combinations
class Solution:
    def validSquare(self, p1, p2, p3, p4) -> bool:
        def minusVec(p1,p2):
            return [p1[0]-p2[0],p1[1]-p2[1]]
        def dotProduct(p1,p2):
            return p1[0]*p2[0] + p1[1] * p2[1]
        def distanceSquare(p1,p2):
            return dotProduct(minusVec(p1,p2),minusVec(p1,p2))
        def isOrthogonal(p1,p2,p3):
            return dotProduct(minusVec(p1,p2),minusVec(p1,p3))==0
        for p,q in combinations([p1,p2,p3,p4],2):
            if p[0]==q[0] and p[1]==q[1]: return False
        sortRest = sorted([p2,p3,p4], key=lambda x:distanceSquare(p1,x))
        for i,(q,r) in enumerate(combinations([p2,p3,p4],2)):
            if isOrthogonal(p1,q,r):
                rest = [p2,p3,p4][2-i]
                #print(q,r,rest)
                if isOrthogonal(q,p1,rest) and isOrthogonal(rest,q,r) and isOrthogonal(r,p1,rest):
                    return distanceSquare(p1,q)==distanceSquare(p1,r)
        else:
            return False