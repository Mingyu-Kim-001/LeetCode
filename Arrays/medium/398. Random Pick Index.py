import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
    def pick(self, target: int) -> int:
        
        def pick_from_a_to_b(target,a,b):
            if a>b: return -1
            if a==b: return a if self.nums[a] == target else -1
            rand = random.randint(a,b)
            if self.nums[rand]==target:
                return rand
            pre = pick_from_a_to_b(target,a,rand-1)
            if pre!=-1: return pre
            post = pick_from_a_to_b(target,rand+1,b)
            return post
        return pick_from_a_to_b(target,0,len(self.nums)-1)