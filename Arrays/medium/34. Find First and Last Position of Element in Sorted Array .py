class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1,-1]
        
        l,r = 0, len(nums) - 1
        end = -1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    end = max(end,mid)
                l = mid + 1
            else:
                r = mid - 1
        
        l,r = 0, len(nums) - 1
        start = float("inf")
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    start = min(start,mid)
                r = mid - 1
            else:
                l = mid + 1
        return [start if start!=float("inf") else -1,end]