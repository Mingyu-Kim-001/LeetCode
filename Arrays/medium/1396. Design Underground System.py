class UndergroundSystem:

    def __init__(self):
        self.cur_check_in = {}
        self.time_sum = defaultdict(lambda:defaultdict(int)) #time_sum[a][b]: sum of time with a->b
        self.count = defaultdict(lambda:defaultdict(int)) #count[a][b]: count of a->b

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cur_check_in[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        depart,depart_t = self.cur_check_in.pop(id)
        self.time_sum[depart][stationName] += t - depart_t
        self.count[depart][stationName] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.time_sum[startStation][endStation] / self.count[startStation][endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)