import math
from City import City
from Flight import Flight
from TimeTable import TimeTable

class Data:
    Paris = City("Paris",48.85,2.35)
    Berlin = City("Berlin",52.52,13.40)
    Hamburg = City("Hamburg",53.55,9.99)
    Munich = City("Munich",48.13,11.58)
    Amsterdam = City("Amsterdam",52.36,4.89)
    Brussels = City("Brussels",50.85,4.35)
    Warsaw = City("Warsaw",52.22,21.01)

    Flights1 = Flight("11:30","1:30",1,["tue","fri"])
    Flights2 = Flight("8:00","10:00",2,["wed","sat"])
    Flights3 = Flight("2:00","3:00",3,["tue","thu"])
    Flights4 = Flight("9:00","10:00",4,["fri","sat"])
    Flights5 = Flight("8:00","10:00",5,["tue","wed"])
    Flights6 = Flight("4:00","5:30",6,["tue","wed"])
    Flights7 = Flight("1:00","2:00",7,["wed","sat"])
    Flights8 = Flight("2:00","5:00",8,["wed"])
    Flights9 = Flight("6:00","9:00",9,["wed"])
    Flights10 = Flight("6:00","8:00",10,["wed","fri"])

    Paris_Berlin = TimeTable(Paris,Berlin,[Flights1,Flights2])
    Paris_Brussels = TimeTable(Paris,Brussels,[Flights9])
    Brussels_Amsterdam = TimeTable(Brussels,Amsterdam,[Flights3,Flights4])
    Amsterdam_Berlin = TimeTable(Amsterdam,Berlin,[Flights3,Flights5])
    Amsterdam_Hamburg = TimeTable(Amsterdam,Hamburg,[Flights6,Flights5])
    Berlin_Munich = TimeTable(Berlin,Munich,[Flights7,Flights8])
    Hamburg_Warsaw = TimeTable(Hamburg,Warsaw,[Flights1,Flights9])
    Munich_Warsaw = TimeTable(Munich,Warsaw,[Flights2,Flights10])

    Cities = [Paris,Berlin,Hamburg,Munich,Amsterdam,Brussels,Warsaw]
    TimeTables = [Paris_Berlin,Paris_Brussels,Brussels_Amsterdam,Amsterdam_Berlin,Amsterdam_Hamburg,Berlin_Munich,Hamburg_Warsaw,Munich_Warsaw]

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

    def calculateTime(self,time1,time2):
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
        daysArray = ["sat","sun","mon","tue","wed","thu","fri"]
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

    def getPrevious(self,Day):
        if Day == "sat":
            return "fri"
        elif Day == "sun":
            return "sat"
        elif Day == "mon":
            return "sun"
        elif Day == "tue":
            return "mon"
        elif Day == "wed":
            return "tue"
        elif Day == "thu":
            return "wed"
        elif Day == "fri":
            return "thu"

    def getNext(self,Day):
        if Day == "sat":
            return "sun"
        elif Day == "sun":
            return "mon"
        elif Day == "mon":
            return "tue"
        elif Day == "tue":
            return "wed"
        elif Day == "wed":
            return "thu"
        elif Day == "thu":
            return "fri"
        elif Day == "fri":
            return "sat"



