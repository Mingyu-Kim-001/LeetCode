class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def DFS(nums,target,path):
            if target < 0:
                return
            if target == 0:
                result.append(path)
            for i in range(len(nums)):
                DFS(nums[i:],target-nums[i],path+[nums[i]])
        
        DFS(candidates,target,[])
        return result