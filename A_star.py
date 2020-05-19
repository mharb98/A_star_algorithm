from Data import  Data

Data1 = Data()
citiesList = Data1.Cities
TimeTableList = Data1.TimeTables

def get_city(element,list):
    for i in range(len(list)):
        if element == list[i].name:
            return list[i]

def getTimetables(City,TimeTables):
    name = City.name
    retList = []
    for i in range(len(TimeTables)):
        if name == TimeTables[i].city1:
            retList.append(TimeTables[i])
    return retList

def checkDays(rangeFlight,Flights):
    retList = []
    for k in range(len(Flights)):
        daysList = Flights[k].days
        for i in range(len(rangeFlight)):
            for j in range(len(daysList)):
                if rangeFlight[i] == daysList[j]:
                    retList.append([daysList[j],Flights[k].departureTime,Flights[k].arrivalTime])
    return retList

def check_intervals(availableList,intervals):
    for i in range(len(availableList)):
        av = availableList[i]
        day = av[0]
        departTime = av[1]
        arrTime = av[2]
        for j in range(len(intervals)):
            day2 = intervals[j][0]
            departTime2 = intervals[j][1]
            arrTime2 = intervals[j][2]
            if day == day2:
                list1 = departTime.split(":")
                list2 = arrTime.split(":")
                list3 = departTime2.split(":")
                list4 = arrTime2.split(":")
                if list1[0] <= list4[0] or list2[0] >= list3[0]:
                    return []
                elif list1[0] == list4[0] and list1[1] <= list4[1]:
                    return []
                elif list2[0] == list3[0] and list2[1] >= list4[1]:
                    return []
            return av
    return availableList[0]

def A_star(departure,destination,totalTime,intervals,rangeFlight,openList):
    if departure == destination:
        for i in range(len(openList)):
            print("Travel from "+ openList[i][0] +" to "+openList[i][1]+" on "+ openList[i][2] + "day between " + openList[i][3] + " : " + openList[i][4])
        return
    departCity = get_city(departure,citiesList)
    citiesList.remove(departCity)
    edges = getTimetables(departCity,TimeTableList)
    dummyHeuristic = 100000
    suitableDay = None
    suitableDepart = None
    suitableArr = None
    suitableTable = None
    for i in range(len(edges)):
        flightsList = edges[i].Flights
        availableList = checkDays(rangeFlight,flightsList)
        if len(availableList) > 0:
            interval = check_intervals(availableList,intervals)
            if len(interval) > 0:
                futureCity = get_city(edges[i].city2,citiesList)
                if futureCity.name == departure:
                    heuristic = Data1.calculateTime(interval[1],interval[2])
                else:
                    heuristic = Data1.calculateDistance(departCity,futureCity) + Data1.calculateTime(interval[1],interval[2])
                if heuristic < dummyHeuristic:
                    dummyHeuristic = heuristic
                    suitableDay = interval[0]
                    suitableTable = edges[i]
                    suitableDepart = interval[1]
                    suitableArr = interval[2]

    newInterval = [suitableDay,suitableDepart,suitableArr]
    intervals.append(newInterval)
    print(departure)
    newOpen = [departure,suitableTable.city2,suitableDay,suitableDepart,suitableArr]
    openList.append(newOpen)
    totalTime = totalTime + Data1.calculateTime(suitableDepart,suitableArr)
    if len(openList) > 0:
        time2 = openList[len(openList)-1][4]
        totalTime = totalTime + Data1.calculateTime(time2,suitableDepart)
    if totalTime >= 12:
        rangeFlight[0] = Data1.getNext(rangeFlight[0])
        totalTime = totalTime - 12
    A_star(suitableTable.city2,destination,totalTime,intervals,rangeFlight,openList)



