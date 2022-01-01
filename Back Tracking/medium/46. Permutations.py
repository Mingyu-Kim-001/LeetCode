class Solution:
    def DFS(self, ans, nums, path):
        if not nums:
            ans.append(path[:])
            
        for i in range(len(nums)):
            path.append(nums[i])
            self.DFS(ans, nums[:i] + nums[i + 1: ], path)
            path.pop()
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.DFS(ans, nums, [])
        return ans