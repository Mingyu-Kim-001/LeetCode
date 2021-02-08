class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        if len(bloomDay)<m*k: return -1
        def canMake(i): #return True if possible to make in ith day
            length_of_adjacent = 0
            num_bouquets = 0
            for day in bloomDay:
                if day<=i:
                    length_of_adjacent+=1
                    if length_of_adjacent%k==0: num_bouquets+=1
                else:
                    length_of_adjacent=0
            return num_bouquets>=m
                        
                        
        l = 0
        r = max(bloomDay)
        while l<=r:
            mid = (l+r)//2
            
            if not canMake(mid):
                l = mid+1
                continue
            else:
                if not canMake(mid-1):
                    return mid
                r = mid-1