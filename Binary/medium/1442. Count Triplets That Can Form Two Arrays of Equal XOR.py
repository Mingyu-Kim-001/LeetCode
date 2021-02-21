#Time: O(n)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefixes = []
        prefix = result = 0
        prefix_seen = {0:[1,-1]} #[index_count,index_sum]
        for k,num in enumerate(arr):
            prefix^=num
            if prefix in prefix_seen:
                n,total = prefix_seen[prefix]
                result+=k*n-total-n
                prefix_seen[prefix] = [n+1,total+k]
            else:
                prefix_seen[prefix] = [1,k]
        return result