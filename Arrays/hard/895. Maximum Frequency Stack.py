from collections import defaultdict
class FreqStack:
    def __init__(self):
        self.nums_in_freq = defaultdict(list)
        self.freq = defaultdict(int)
        self.max_freq = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        self.nums_in_freq[self.freq[x]].append(x)
        self.max_freq = max(self.max_freq, self.freq[x])
        
    def pop(self) -> int:
        ans = self.nums_in_freq[self.max_freq].pop()
        if not self.nums_in_freq[self.max_freq]:
            self.max_freq -= 1
        self.freq[ans] -= 1
        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()