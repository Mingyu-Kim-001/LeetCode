class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        ans = []
        nums.sort()
        i, j = 0, 1
        while i < len(nums) - 3:
            j = i + 1
            
            while j < len(nums) - 2:
                k, l = j + 1, len(nums) - 1
                
                while k < l:
                    
                    # print(i,j,k,l)
                    cur_sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if cur_sum == target:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        while k < len(nums) - 1 and nums[k+1] == nums[k]:
                            k += 1
                        while k < l and nums[l-1] == nums[l]:
                            l -= 1
                        k += 1
                        l -= 1
                    elif cur_sum < target:
                        k += 1
                    else:
                        l -= 1
                    
                while j < len(nums) - 2 and nums[j+1] == nums[j]:
                    j += 1
                j += 1
            
            while i < len(nums) - 3 and nums[i+1] == nums[i]:
                i += 1
            i += 1
            
        return ans