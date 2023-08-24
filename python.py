class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights_by_city(self, city):
        results = [flight for flight in self.flights if city in (flight.source, flight.destination)]
        return results

    def search_flights_from_city(self, city):
        results = [flight for flight in self.flights if flight.source == city]
        return results

    def search_flights_between_cities(self, city1, city2):
        results = [flight for flight in self.flights if (flight.source == city1 and flight.destination == city2) or
                   (flight.source == city2 and flight.destination == city1)]
        return results

def main():
    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    flight_table = FlightTable()

    for data in flight_data:
        flight = Flight(*data)
        flight_table.add_flight(flight)

    cities = {
        "BLR": "Bengaluru",
        "BOM": "Mumbai",
        "BBI": "Bhubaneswar",
        "HYD": "Hyderabad",
        "JLR": "Jabalpur"
    }

    print("Choose search parameter:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input())

    if choice == 1:
        city_code = input("Enter city code: ")
        city_name = cities.get(city_code, "Unknown City")
        results = flight_table.search_flights_by_city(city_code)
    elif choice == 2:
        city_code = input("Enter city code: ")
        city_name = cities.get(city_code, "Unknown City")
        results = flight_table.search_flights_from_city(city_code)
    elif choice == 3:
        city_code1 = input("Enter first city code: ")
        city_name1 = cities.get(city_code1, "Unknown City")
        city_code2 = input("Enter second city code: ")
        city_name2 = cities.get(city_code2, "Unknown City")
        results = flight_table.search_flights_between_cities(city_code1, city_code2)
    else:
        print("Invalid choice!")
        return

    print(f"Flights for {city_name}:")
    for flight in results:
        print(f"Flight ID: {flight.flight_id}, From: {cities[flight.source]}, To: {cities[flight.destination]}, Price: {flight.price}")

if __name__ == "__main__":
    main()
