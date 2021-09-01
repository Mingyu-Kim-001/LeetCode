class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        visit = set()
        def DFS(num, length):
            if num in visit:
                return length
            visit.add(num)
            return DFS(nums[num], length+1)
        
        ans = 0
        for num in nums:
            if not num in visit:
                ans = max(ans, DFS(num, 0))
        
        return ans
                
                