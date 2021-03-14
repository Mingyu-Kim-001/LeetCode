#Time: O(n^2)
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = pow(10,9) + 7
        arr.sort()
        treeCount = {}
        for num in arr:
            treeCount[num] = 1
            for i in treeCount:
                if num % i == 0 and num // i in treeCount:
                    treeCount[num] += treeCount[num//i] * treeCount[i]
        return sum(treeCount.values()) % MOD