class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for numberOfBoxes, numberOfUnitsPerBox in boxTypes:
            if truckSize >= numberOfBoxes:
                ans += numberOfBoxes * numberOfUnitsPerBox
                truckSize -= numberOfBoxes
            else:
                ans += truckSize * numberOfUnitsPerBox
                break
        return ans