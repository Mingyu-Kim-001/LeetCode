class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        m = max(instructions)
        bit = [0]*(m+1)
        
        def update(a):
            while a<=m:
                bit[a]+=1
                a+= a & -a
        def get(a):
            res = 0
            while a>0:
                res+=bit[a]
                a-= a&-a
            return res
        res = 0
        for i,a in enumerate(instructions):
            res+= min(get(a-1),i-get(a))
            update(a)
        return res%(pow(10,9)+7)