from collections import Counter
import heapq as hq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        remaining = []
        for barcode, count in counter.items():
            remaining.append([-count, barcode])
        hq.heapify(remaining)
        ans = []
        while remaining:
            minus_count, barcode = hq.heappop(remaining)
            if ans and ans[-1] == barcode:
                minus_count2, barcode2 = hq.heappop(remaining)
                ans.append(barcode2)
                if minus_count2 + 1 < 0:
                    hq.heappush(remaining, [minus_count2 + 1, barcode2])
                hq.heappush(remaining, [minus_count, barcode])
            else:
                ans.append(barcode)
                if minus_count + 1 < 0:
                    hq.heappush(remaining, [minus_count + 1, barcode])
        return ans