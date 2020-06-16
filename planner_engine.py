from data import  Data


class PlannerEngine:

    def __init__(self):
        self.Data1 = Data()
        self.citiesList = self.Data1.Cities.copy()
        self.TimeTableList = self.Data1.TimeTables.copy()

    def get_city(self, element, list):
        for i in range(len(list)):
            if element == list[i].name:
                return list[i]

    def getTimetables(self, city, timetables):
        name = city.name
        retList = []
        for i in range(len(timetables)):
            if name == timetables[i].city1:
                retList.append(timetables[i])
        return retList

    def checkDays(self, rangeFlight, Flights):
        retList = []
        days = ['sat', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri']
        for k in range(len(Flights)):
            daysList = Flights[k].days
            for i in range(len(rangeFlight)):
                for j in range(len(daysList)):
                    if days.index(rangeFlight[i]) >= days.index(daysList[j]):
                        retList.append([daysList[j],Flights[k].departureTime,Flights[k].arrivalTime])
        return retList

    def check_intervals(self, availableList, intervals):
        for i in range(len(availableList)):
            av = availableList[i]
            day = av[0]
            departTime = av[1]
            for j in range(len(intervals)):
                day2 = intervals[j][0]
                arrTime2 = intervals[j][2]
                if day == day2:
                    newDepart = departTime.split(":")
                    prevArrive = arrTime2.split(":")
                    if newDepart <= prevArrive:
                        return []
                return av
        return availableList[0]

    def A_star(self, departure, destination, totalTime, intervals, rangeFlight, openList):
        if departure == destination:
            for i in range(len(openList)):
                print("Travel from "+ openList[i][0] +" to "+openList[i][1]+" on "+ openList[i][2] + " day between " + openList[i][3] + " : " + openList[i][4])
            return
        departCity = self.get_city(departure, self.citiesList)
        self.citiesList.remove(departCity)
        edges = self.getTimetables(departCity, self.TimeTableList)
        dummyHeuristic = 100000
        suitableDay = None
        suitableDepart = None
        suitableArr = None
        suitableTable = None
        for i in range(len(edges)):
            flightsList = edges[i].Flights
            availableList = self.checkDays(rangeFlight, flightsList)
            if len(availableList) > 0:
                interval = self.check_intervals(availableList, intervals)
                if len(interval) > 0:
                    futureCity = self.get_city(edges[i].city2, self.citiesList)
                    if futureCity.name == departure:
                        heuristic = self.Data1.calculateTime(interval[1], interval[2])
                    else:
                        heuristic = self.Data1.calculateDistance(departCity, futureCity) + self.Data1.calculateTime(interval[1],interval[2])
                    if heuristic < dummyHeuristic:
                        dummyHeuristic = heuristic
                        suitableDay = interval[0]
                        suitableTable = edges[i]
                        suitableDepart = interval[1]
                        suitableArr = interval[2]

        newInterval = [suitableDay,suitableDepart,suitableArr]
        intervals.append(newInterval)
        newOpen = [departure,suitableTable.city2,suitableDay,suitableDepart,suitableArr]
        openList.append(newOpen)
        totalTime = totalTime + self.Data1.calculateTime(suitableDepart,suitableArr)
        if len(openList) > 0:
            time2 = openList[len(openList)-1][4]
            totalTime = totalTime + self.Data1.calculateTime(time2,suitableDepart)
        if totalTime >= 12:
            rangeFlight[0] = self.Data1.getNext(rangeFlight[0])
            totalTime = totalTime - 12
        self.A_star(suitableTable.city2, destination, totalTime, intervals, rangeFlight, openList)

    def travel(self, departure, destination, interval):
        print('Steps for travelling from {} to {}:'.format(departure, destination))
        self.A_star(departure, destination, 0, [], interval, [])
        print('----------------------')