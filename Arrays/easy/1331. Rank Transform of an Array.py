class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        uniqueSortedList = sorted(list(set(arr)))
        idx_value_dic = {j:i+1 for i,j in enumerate(uniqueSortedList)}
        return [idx_value_dic[i] for i in arr]
        