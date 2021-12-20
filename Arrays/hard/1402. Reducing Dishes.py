#Time: O(n)
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        satisfaction_ge0 = [i for i in satisfaction if i>=0]
        satisfaction_l0 = [i for i in satisfaction if i<0]
        total = sum(satisfaction_ge0)
        result = 0
        for i,num in enumerate(satisfaction_ge0):
            result+=(i+1)*num
        for num in satisfaction_l0[::-1]:
            if -num<total:
                total+=num
                result+=total
            else:
                break
        return result