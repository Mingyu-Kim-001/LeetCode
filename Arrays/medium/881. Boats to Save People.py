from collections import deque
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = deque(sorted(people))
        result = 0
        while people:
            if len(people)==1:
                result+=1
                break
            if people[-1]+people[0]<=limit:
                people.popleft()
                people.pop()
            else:
                people.pop()
            result+=1
                
        return result