#Time: O(nlogn)
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def isPossible(capacity):
            weightSum = 0
            n_ship = 0
            for weight in weights:
                if weight>capacity: return False
                
                if weight+weightSum>capacity:
                    n_ship+=1
                    weightSum = weight
                else:
                    weightSum+=weight
            return n_ship<D
        l,r = 0,sum(weights)
        # print(isPossible(11))
        while l<r:
            m = (l+r)//2
            if isPossible(m):
                if not isPossible(m-1): return m
                r = m-1
            else:
                if isPossible(m+1): return m+1
                l = m+1