class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        can_visit = [0]
        while can_visit:
            visiting = can_visit.pop()
            if visiting in visited:
                continue
            for key in rooms[visiting]:
                if not key in visited:
                    can_visit.append(key)
            visited.add(visiting)
        return len(visited) == len(rooms)