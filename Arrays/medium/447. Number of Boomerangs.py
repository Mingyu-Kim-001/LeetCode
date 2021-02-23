#Time: O(n^2)
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p1,p2):
            return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        result = 0
        for i in range(len(points)):
            distDic = defaultdict(int)
            for j in range(len(points)):
                if i==j:continue
                d = distance(points[i],points[j])
                distDic[d]+=1
            for d in distDic:
                if distDic[d]>1:
                    result+=distDic[d]*(distDic[d]-1)
        return result