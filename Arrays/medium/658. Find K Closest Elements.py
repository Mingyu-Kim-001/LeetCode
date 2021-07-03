class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if arr[0] >= x:
            return arr[:k]
        if arr[-1] <= x:
            return arr[-k:]
        
        for i, num in enumerate(arr):
            if num > x:
                l = i - 1
                r = i
                break
        while r - l - 1 < k:
            if 0 <= l < r < len(arr):
                if x - arr[l] > arr[r] - x:
                    r += 1
                else:
                    l -= 1
            elif l >= 0:
                l -= 1
            else:
                r += 1
        return arr[l+1:r]