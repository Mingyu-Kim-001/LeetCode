class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result = []
        l,r = 1,k+1
        while l < r:
            result.append(l)
            result.append(r)
            l += 1
            r -= 1
        if l == r:
            result.append(l)
        return result + list(range(k+2,n+1))
            