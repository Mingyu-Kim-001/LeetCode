class Trie:
    def __init__(self):
        self.descendant = {}
        self.val = 0
        self.sum_descendant = 0

class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        
        def DFS(cur_trie, key, key_idx, val):
            c = key[key_idx]
            if not c in cur_trie.descendant:
                cur_trie.descendant[c] = Trie()
                
            cur_trie = cur_trie.descendant[c]
            if key_idx == len(key) - 1:
                diff = val - cur_trie.val
                cur_trie.val = val
                cur_trie.sum_descendant += diff
            else:
                diff = DFS(cur_trie, key, key_idx+1, val)
                cur_trie.sum_descendant += diff
            return diff
        
        DFS(self.trie, key, 0, val)
        
    def sum(self, prefix: str) -> int:
        cur_trie = self.trie
        for c in prefix:
            if not c in cur_trie.descendant:
                return 0
            cur_trie = cur_trie.descendant[c]
        return cur_trie.sum_descendant
            


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)