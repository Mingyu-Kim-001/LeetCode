class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a,b):
            small = min(a,b)
            big = max(a,b)
            if big%small==0: return small
            return gcd(small,big%small)
        result = []
        for i in range(2,n+1):
            for j in range(1,i):
                if gcd(i,j)==1:
                    result.append(str(j)+"/"+str(i))
        return result