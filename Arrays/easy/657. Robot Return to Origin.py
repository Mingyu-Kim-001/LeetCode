class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u,l = 0,0
        for move in moves:
            if move=="U":
                u+=1
            elif move=="D":
                u-=1
            elif move=="L":
                l+=1
            else:
                l-=1
        return u==0 and l==0