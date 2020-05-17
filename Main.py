from City import City
from Flight import Flight
from TimeTable import TimeTable

City1 = City("Cairo",123,456)
City2 = City("Casablanca",678,856)
Days1 = ["Tue","Fri"]
Days2 = ["Sun","Wed"]
Flight1 = Flight(11.30,12.40,1,Days1)
Flight2 = Flight(1.30,3.30,2,Days2)

FlightList = [Flight1,Flight2]

TimeTable1 = TimeTable(City1,City2,FlightList)

print(City1.latitude)
print(City1.longitude)
print(City2.name)
print(Flight1.departure)
print(Flight1.destination)
print(Flight1.number)
print(Flight2.days)
print(TimeTable1.city1)
print(TimeTable1.city2)
print(TimeTable1.Flights[0].days)