class Solution:
    def countBits(self, num: int) -> List[int]:
        if num==0: return [0]
        if num==1: return [0,1]
        i = 0
        result = [0]
        while (1<<i)<=num:
            result = result + [j+1 for j in result]
            i+=1
        return result[:num+1]