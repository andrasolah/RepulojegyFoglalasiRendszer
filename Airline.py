from Flight import Flight

class Airline:
    def __init__(self, name: str, code: str):
        self._name = name
        self._code = code
        self._flights = []

    @property
    def name(self):
        return self._name

    @property
    def code(self):
        return self._code
    
    @property
    def flights(self):
        return self._flights
    
    def print_flights(self, formatted: bool = False):
        print(f"{'Flight':<10}|{'Departure City / Country':<25}|{'Departure Airport':<20}|{'Arrival City / Country':<25}|{'Arrival Airport':<20}|{'Price (Ft)':<15}|{'Flight Date & Time':<10}")
        
        for flight in self._flights:
            print(flight.get_flight_details(formatted))
    
    def add_flight(self, flight: Flight):
        self._flights.append(flight)


