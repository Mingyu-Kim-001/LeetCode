class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        n_z = (k-n)//25
        remaining = (k - 26*n_z) - (n-n_z)
        if n==n_z: return "z"*n_z
        result = "a"*(n-n_z-1) + chr(ord("a") + remaining) + "z"*n_z
        return result