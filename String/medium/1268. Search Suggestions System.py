class Solution:
    def DFS(self, cur_trie, prefix, result_list):
        if len(result_list) >= 3:
            return
        
        if "END" in cur_trie:
            result_list.append(prefix)
                
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c in cur_trie:
                self.DFS(cur_trie[c], prefix+c, result_list)
            
        
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = defaultdict(list)
        for product in products:
            cur_trie = trie
            for char in product:
                if not char in cur_trie:
                    cur_trie[char] = {}
                cur_trie = cur_trie[char]
            cur_trie["END"] = True
        
        cur_trie = trie
        ans = [[] for _ in range(len(searchWord))]
        prefix = ""
        
        for i,c in enumerate(searchWord):
            prefix += c
            if not c in cur_trie:
                break
            cur_trie = cur_trie[c]    
            self.DFS(cur_trie, prefix, ans[i])
            
        
        return ans