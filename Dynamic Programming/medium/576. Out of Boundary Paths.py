class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        MOD = pow(10,9)+7
        result = 0
        dp = defaultdict(int)
        dp[(i,j)]=1

        for k in range(N):
            dp2 = defaultdict(int)
            for p in range(m):
                for q in range(n):
                    if p!=0:
                        dp2[(p,q)] = (dp2[(p,q)] + dp[(p-1,q)])%MOD
                    else:
                        result = (result+dp[(p,q)])%MOD
                    if q!=0:
                        dp2[(p,q)] = (dp2[(p,q)] +dp[(p,q-1)])%MOD
                    else:
                        result = (result+dp[(p,q)])%MOD
                    if p!=m-1:
                        dp2[(p,q)] = (dp2[(p,q)] +dp[(p+1,q)])%MOD
                    else:
                        result = (result+dp[(p,q)])%MOD
                    if q!=n-1:
                        dp2[(p,q)] = (dp2[(p,q)] +dp[(p,q+1)])%MOD
                    else:
                        result = (result+dp[(p,q)])%MOD
            dp = dp2
        return result%MOD