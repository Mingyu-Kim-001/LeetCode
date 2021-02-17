class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if C<=E or G<=A or H<=B or D<=F: return (C-A)*(D-B)+(G-E)*(H-F)
        x = min(C,G) - max(A,E)
        y = min(D,H) - max(B,F)
        return (C-A)*(D-B)+(G-E)*(H-F)-x*y