class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(S):
            result = ""
            for i in range(len(S)):
                result+= "0" if S[i]=="1" else "1"
            return result
        S = "0"
        for i in range(n-1):
            S = S + "1" + invert(S)[::-1]
#         print(S)
        return S[k-1]