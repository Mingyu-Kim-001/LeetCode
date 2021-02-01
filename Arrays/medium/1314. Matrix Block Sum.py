#Time: O(mn)
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        prefix = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                prefix[i][j] = mat[i-1][j-1] + prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1]
                
        answer = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                    
                answer[i][j] = (prefix[min(i+K+1,m)][min(j+K+1,n)] - 
                                prefix[max(i-K,0)][min(j+K+1,n)] - 
                                prefix[min(i+K+1,m)][max(j-K,0)] + 
                                prefix[max(i-K,0)][max(j-K,0)]
                               )
                
        return answer