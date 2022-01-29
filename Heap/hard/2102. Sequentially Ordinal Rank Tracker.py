import heapq
class MaxHeapObj(object):
    def __init__(self, score_and_name):
        score, name = score_and_name
        self.score = score
        self.name = name
    def __lt__(self, other): 
        return self.score > other.score or (self.score == other.score and self.name < other.name)
    def __eq__(self, other): 
        return self.score == other.score and self.name == other.name
    def __str__(self): return str((self.score, self.name))
    def to_tuple(self): return (self.score, self.name)
    
class MinHeapObj(object):
    def __init__(self, score_and_name):
        score, name = score_and_name
        self.score = score
        self.name = name
    def __lt__(self, other): 
        return self.score < other.score or (self.score == other.score and self.name > other.name)
    def __eq__(self, other): 
        return self.score == other.score and self.name == other.name
    def __str__(self): return str((self.score, self.name))
    def to_tuple(self): return (self.score, self.name)
    
class MinHeap(object):
    def __init__(self): self.h = []
    def heappush(self, x): heapq.heappush(self.h, MinHeapObj(x))
    def heappop(self): return heapq.heappop(self.h)
    def __getitem__(self, i): return self.h[i]
    def __len__(self): return len(self.h)
    def __str__(self): return str([str(obj) for obj in self.h])

class MaxHeap(MinHeap):
    def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
    
class SORTracker:
    def __init__(self):
        self.pre_heap = MinHeap()
        self.post_heap = MaxHeap()

    def add(self, name: str, score: int) -> None:
        if not self.pre_heap or self.pre_heap[0].score > score or (self.pre_heap[0].score == score and self.pre_heap[0].name < name):
            self.post_heap.heappush((score, name))
        else:
            self.post_heap.heappush(self.pre_heap.heappop().to_tuple())
            self.pre_heap.heappush((score, name))
        # print("add", self.pre_heap, self.post_heap)
        
    def get(self) -> str:
        self.pre_heap.heappush(self.post_heap.heappop().to_tuple())
        # print("get", self.pre_heap, self.post_heap, self.pre_heap[0].name)
        return self.pre_heap[0].name


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()