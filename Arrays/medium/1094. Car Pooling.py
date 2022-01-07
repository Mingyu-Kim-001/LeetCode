class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        descending_by_end = sorted(trips, key=lambda x:x[2], reverse=True)
        descending_by_start = sorted(trips, key=lambda x:x[1], reverse=True)
        current_passengers = 0
        while descending_by_end:
            outflow, _, to = descending_by_end.pop()
            while descending_by_start and descending_by_start[-1][1] < to:
                inflow, _, _ = descending_by_start.pop()
                current_passengers += inflow
                if current_passengers > capacity:
                    return False
            current_passengers -= outflow
        return True