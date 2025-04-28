from Flight import Flight
from datetime import datetime

class DomesticFlight(Flight):
    def __init__(self, flight_number: str, departure_airport: str, arrival_airport: str, price: int, departure_datetime: datetime, departure_city: str, arrival_city: str):
        super().__init__(flight_number, departure_airport, arrival_airport, price, departure_datetime)
        self._departure_city = departure_city
        self._arrival_city = arrival_city

    #getters for the properties
    @property
    def flight_number(self):
        return self._flight_number
    
    @property
    def departure_airport(self):
        return self._departure_airport
    
    @property
    def arrival_airport(self):
        return self._arrival_airport
    
    @property
    def price(self):
        return self._price
    
    @property
    def departure_datetime(self):
        return self._departure_datetime
    
    @property
    def departure_city(self):
        return self._departure_city
    
    @property
    def arrival_city(self):
        return self._arrival_city
    
    #setters for the properties
    @departure_airport.setter
    def departure_airport(self, departure_airport: str):
        self._departure_airport = departure_airport
    
    @arrival_airport.setter
    def arrival_airport(self, arrival_airport: str):
        self._arrival_airport = arrival_airport
        
    @price.setter
    def price(self, price: int):
        self._price = price
    
    @departure_datetime.setter
    def departure_datetime(self, departure_datetime: datetime):
        self._departure_datetime = departure_datetime
    
    @departure_city.setter
    def departure_city(self, departure_city: str):
        self._departure_city = departure_city
        
    @arrival_city.setter
    def arrival_city(self, arrival_city: str):
        self._arrival_city = arrival_city

    def get_flight_details(self, formatted: bool = False):
        if formatted:
            return f"{self._flight_number:<10}|{self._departure_city:<25}|{self._departure_airport:<20}|{self._arrival_city:<25}|{self._arrival_airport:<20}|{self._price:<15}|{self._departure_datetime.strftime('%Y-%m-%d %H:%M'):<10}"
        else:
            return {
                "Flight Number": self._flight_number,
                "Departure City": self._departure_city,
                "Departure Airport": self._departure_airport,
                "Arrival City": self._arrival_city,
                "Arrival Ariport": self._arrival_airport,
                "Price": str(self._price) + "Ft",
                "Departure date & time": self._departure_datetime.strftime("%Y-%m-%d %H:%M")
            }
        
    def get_destination(self):
        return self._arrival_city
