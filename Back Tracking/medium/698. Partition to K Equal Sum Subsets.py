class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k or sum(nums) % k:
            return False
        target = [sum(nums) // k] * k
        nums.sort(reverse=True)
        def DFS(idx):
            if idx == len(nums):
                return True
            for i in range(k):
                if target[i] >= nums[idx]:
                    target[i] -= nums[idx]
                    if DFS(idx+1):
                        return True
                    target[i] += nums[idx]
            return False
        return DFS(0)