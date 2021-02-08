class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        
        first = result = float("-inf")
        for i,a in enumerate(A):
            
            if i!=0:
                result = max(result,first+a-i)
            first = max(first,a+i)
            #print(first,result)
        return result