class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        hap = [(i,j,i+j ) for i,j in zip(aliceValues,bobValues)]
        hap = sorted(hap,reverse=True,key=lambda x:x[2])
        aliceSums = sum([i[0] for i in hap[::2]])
        bobSums = sum([i[1] for i in hap[1::2]])
        if aliceSums>bobSums: return 1
        elif aliceSums<bobSums: return -1
        return 0