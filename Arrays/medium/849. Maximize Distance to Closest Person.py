#Time: O(n)
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev = maxDistance = -1
        for i,seat in enumerate(seats):
            if seat:
                if prev<0 and seats[0]==0:
                    maxDistance = i
                else:
                    d = (prev+i)//2 - prev
                    maxDistance = max(maxDistance,d)
                prev = i
        maxDistance = max(maxDistance,len(seats)-1-prev)
        return maxDistance