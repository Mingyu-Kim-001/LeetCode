class Solution:
    def shipWithinDays(self, weights,D: int) -> int:
#         prefixSums = weights[0]
#         for i in range(1,len(weights)):
#             prefixSums.append(prefixSums[-1]+weights[i])

        def isPossible(weights,D,capacity):
            if max(weights)>capacity: return False
            day = 0
            partSum = 0
            for i in range(len(weights)):
                if weights[i]+partSum<=capacity:
                    partSum+= weights[i]
                else:
                    partSum = weights[i]
                    day+=1
                if day>=D:
                    return False
                #print(weights[i],partSum,day)
            return True
        left = 0
        right = sum(weights)
        while left<right:
            mid = (left+right)//2
            if isPossible(weights,D,mid):
                if not isPossible(weights,D,mid-1):
                    return mid
                else:
                    right = mid - 1
            else:
                if isPossible(weights,D,mid+1):
                    return mid+1
                else:
                    left = mid + 1