import math
from City import City
from Flight import Flight
from TimeTable import TimeTable

class Data:
    City1 = City("Cairo",123,456)
    City2 = City("Casablanca",678,856)
    Days1 = ["tue","fri"]
    Days2 = ["sun","wed"]
    Flight1 = Flight("11:30","12:40",1,Days1)
    Flight2 = Flight("1:30","3:30",2,Days2)

    FlightList = [Flight1,Flight2]

    TimeTable1 = TimeTable(City1,City2,FlightList)

    Cities = [City1,City2]
    TimeTables = [TimeTable1]

    def calculateDistance(self,departure,destination):
        earth_radius = 6373.0
        latitude1 = math.radians(departure.latitude)
        latitude2 = math.radians(destination.latitude)
        longitude1 = math.radians(departure.longitude)
        longitude2 = math.radians(destination.longitude)

        difference_latitude = abs(latitude1-latitude2)
        difference_longitude = abs(longitude1-longitude2)

        dummy = math.sin(difference_latitude / 2) ** 2 + math.cos(latitude1) * math.cos(latitude2) * math.sin(difference_longitude / 2) ** 2

        dummy2 = 2 * math.atan2(math.sqrt(dummy), math.sqrt(1 - dummy))

        return earth_radius*dummy2

    def calculateTime(self,flight1):
        time1 = flight1.departure
        time2 = flight1.destination
        time1_list = time1.split(":")
        time2_list = time2.split(":")
        dummy1 = abs(int(time1_list[0]) - int(time2_list[0]))
        dummy2 = abs(int(time1_list[1]) - int(time2_list[1]))/60

        return dummy1 + dummy2

    def mapDays(self,Day):
        if Day == "Sunday":
            return "sun"
        elif Day == "Monday":
            return "mon"
        elif Day == "Tuesday":
            return "tue"
        elif Day == "Wednesday":
            return "wed"
        elif Day == "Thursday":
            return "thu"
        elif Day == "Friday":
            return "fri"
        else:
            return "sat"

    def getRange(self,Day1,Day2):
        daysArray = ["sun","mon","tue","wed","thu","fri","sat"]
        index1 = daysArray.index(Day1)
        index2 = daysArray.index(Day2)
        retList = []
        retList2 = []
        if index1 == index2:
            retList = [Day1]
            return retList
        elif index1 < index2:
            for i in range(len(daysArray)):
                if i>=index1 and i<=index2:
                    retList.append(daysArray[i])
            return retList
        else:
            for i in range(len(daysArray)):
                if i>=index2 and i<=index1:
                    retList.append(daysArray[i])
            retList2.append(Day1)
            for i in range(len(daysArray)):
                if daysArray[i] not in retList:
                    retList2.append(daysArray[i])
            retList2.append(Day2)
            return retList2

    def getBeforeAfter(self,Day):
        if Day == "sat":
            return ["fri","sun"]
        elif Day == "sun":
            return ["sat","mon"]
        elif Day == "mon":
            return ["sun","tue"]
        elif Day == "tue":
            return ["mon","wed"]
        elif Day == "wed":
            return ["tue","thu"]
        elif Day == "thu":
            return ["wed","fri"]
        elif Day == "fri":
            return ["thu","sat"]




