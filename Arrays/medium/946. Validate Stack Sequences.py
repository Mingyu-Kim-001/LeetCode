#Time: O(n)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        queue_idx = 0
        pushed2 = []
        for num in pushed:
            pushed2.append(num)
            while pushed2 and pushed2[-1]==popped[queue_idx]:
                pushed2.pop()
                queue_idx+=1
        if pushed2 or queue_idx<len(popped): return False
        return True