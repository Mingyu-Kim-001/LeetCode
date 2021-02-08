class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k>3*(2**(n-1)): return ""
        prev = (k-1) // (2**(n-1))
        prev_str = chr(ord('a')+prev)
        n-=1
        k = (k-1)%(2**n)
        candidate = {0:["b","c"],1:["a","c"],2:["a","b"]}
        while n>0:
            curr = k // (2**(n-1))
            prev_str = prev_str + candidate[prev][curr]
            n-=1
            k = k%(2**n)
            prev = ord(candidate[prev][curr]) - ord("a")
        return prev_str