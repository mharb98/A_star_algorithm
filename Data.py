import math
from City import City
from Flight import Flight
from TimeTable import TimeTable

class Data:
    City1 = City("Cairo",123,456)
    City2 = City("Casablanca",678,856)
    Days1 = ["Tue","Fri"]
    Days2 = ["Sun","Wed"]
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



