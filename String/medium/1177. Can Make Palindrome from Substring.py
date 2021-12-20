#Time: O(n)
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        count = {}
        for i in "abcdefghijklmnopqrstuvwxyz":
            count[i]=[0]*len(s)
        for i,c in enumerate(s):
            if i==0:count[c][0] = 1
            else:
                for j in "abcdefghijklmnopqrstuvwxyz":
                    count[j][i] = count[j][i-1] + int(j==c)
        result = []
        for left,right,k in queries:
            odd_count = 0
            for j in "abcdefghijklmnopqrstuvwxyz":
                odd_count+=(count[j][right]-(count[j][left-1] if left>0 else 0))%2
                if odd_count//2>k:
                    result.append(False)
                    break
            else:
                result.append(True)
        return result