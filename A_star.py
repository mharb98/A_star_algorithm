from Data import  Data

Data1 = Data()
citiesList = Data1.Cities
TimeTableList = Data1.TimeTables

def get_city(element,list):
    for i in range(len(list)):
        if element == list[i].name:
            return list[i]

def check_interval(interval,times):
    day = interval[0]
    first = interval[1]
    second = interval[2]
    for i in times:
        dummy = times[i]
        if day == dummy[0]:
            list1 = dummy[1].split(":")
            list2 = dummy[2].split(":")
            list3 = first.split(":")
            list4 = second.split(":")
            if list1[0] == list4[0]:
                if list1[1] > list4[1]:
                    return False
            elif list1[0] == list4[0]:
                if list2[1] < list3[1]:
                    return False
            elif list2[0] >= list3[0] or list1[0] <=list4[0]:
                return False
    return True


def get_timetable(departure,destination,rangeFlight,intervals,list):
    for i in range(len(list)):
        if departure == list[i].departure and destination == list[i].destination:
            dummy = list[i]
    Flights = dummy.Flights
    for i in range(len(Flights)):
        days = Flights[i].days
        if rangeFlight[0] in days or rangeFlight[1] in days:
            for day in range(len(days)):
                list = [day[i],Flights[i].departure,Flights[i].destination]
                if check_interval(list,intervals):
                    return [day,Flights[i]]
    return []


def time_difference(first_time,second_time):
    first_time = 5

def A_star(citiesList,departure,destination,rangeFlight,open,totalTime,intervals):
    if departure == destination:
        return open
    start = get_city(departure,citiesList)
    citiesList.remove(start)
    heuristic = 100000
    theFlight = None
    theCountry = None
    day = None
    flighTime = 0
    heuristicList = []
    for i in range(len(citiesList)):
        next = citiesList[i]
        dummyDistance = Data1.calculateDistance(start,next)
        if get_timetable(departure,next.name,rangeFlight,open,TimeTableList)==[]:
            day1 = Data1.getPrevious(rangeFlight[0])
            day2 = Data1.getNext(rangeFlight[1])
            newRange = [day1,day2]
            [day, FlightDummy] = get_timetable(departure, next.name, newRange , open, TimeTableList)
        else:
            [day,FlightDummy] = get_timetable(departure,next.name,rangeFlight,open,TimeTableList)
        timeDummy = Data1.calculateTime(FlightDummy)
        dummyHeuristic = totalTime + dummyDistance + timeDummy
        if dummyHeuristic < heuristic:
            theFlight = FlightDummy
            heuristic = dummyHeuristic
            flighTime = timeDummy
            theCountry = next.name
    heuristicList.append(heuristic)
    totalTime = totalTime + flighTime
    if len(open) > 0:
        extraTime = open[len(open)-2][3]
        totalTime = totalTime + time_difference(extraTime,theFlight.departure)
        if totalTime >= 12:
            totalTime = 0;
            rangeFlight[0] = Data1.getNext(rangeFlight[0])
    dummyList = [day,theFlight.departure,theFlight.destination]
    otherList = [departure,theCountry,day,theFlight.departure,theFlight.destination]
    open.append(otherList)
    intervals.append(dummyList)
    A_star(citiesList,theCountry,destination,rangeFlight,open,totalTime,intervals)
