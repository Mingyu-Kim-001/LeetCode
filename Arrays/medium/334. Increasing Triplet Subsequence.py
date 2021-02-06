#Time:O(n)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        triplet = [float("inf"),float("inf")]
        for num in nums:
            # print(triplet)
            if num<triplet[0]:triplet[0] = num
            elif triplet[0]<num<triplet[1]: triplet[1] = num
            elif triplet[1]<num: return True
        return False