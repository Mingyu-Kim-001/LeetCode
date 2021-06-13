from collections import deque

class Solution:
    
    def next_codes(self,cur_code):
        next_codes_list = []
        for i in range(4):
            next_codes_list.append(cur_code[:i] + str((int(cur_code[i])+1)%10) + cur_code[i+1:])
            next_codes_list.append(cur_code[:i] + str((int(cur_code[i])-1)%10) + cur_code[i+1:])
        
        return next_codes_list
            
    def openLock(self, deadends: List[str], target: str) -> int:
        visit_or_deadends = set(deadends)
        
        bfs = deque()
        bfs.append(["0000",0])
        
        while bfs:
            cur_code, count = bfs.popleft()
            
            if cur_code in visit_or_deadends:
                continue
                
            if cur_code  == target:
                return count
            
            visit_or_deadends.add(cur_code)
            
            for code in self.next_codes(cur_code):
                if not code in visit_or_deadends:
                    bfs.append([code,count+1])
                    
        return -1