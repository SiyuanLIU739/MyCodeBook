class UndergroundSystem:

    def __init__(self):
        self.checked = {}
        self.books = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if(id not in self.checked.keys()):
            self.checked[id] = {'station': "", 't': -1}

        self.checked[id]['station'] = stationName
        self.checked[id]['t'] = t 

    
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.checked[id]['station']
        startTime = self.checked[id]['t']

        if((startStation, stationName) not in self.books.keys()):
            self.books[(startStation, stationName)] = []

        self.books[(startStation, stationName)].append(t - startTime)

        self.checked[id]['station'] = ""
        self.checked[id]['t'] = -1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        n = len(self.books[(startStation, endStation)])
        sumTime = sum(self.books[(startStation, endStation)])

        return sumTime / n