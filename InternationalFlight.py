from Flight import Flight
from datetime import datetime

class InternationalFlight(Flight):
    def __init__(self, flight_number: str, departure_airport: str, arrival_airport: str, price: int, departure_datetime: datetime, departure_country: str, arrival_country: str):
        super().__init__(flight_number, departure_airport, arrival_airport, price, departure_datetime)
        self._departure_country = departure_country
        self._arrival_country = arrival_country

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
    def departure_country(self):
        return self._departure_country
    
    @property
    def arrival_country(self):
        return self._arrival_country
    
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
        
    @departure_country.setter
    def departure_country(self, departure_country: str):
        self._departure_country = departure_country
        
    @arrival_country.setter
    def arrival_country(self, arrival_country: str):
        self._arrival_country = arrival_country
        
    def get_flight_details(self):
        return {
            "Flight Number": self._flight_number,
            "Departure Country": self._departure_country,
            "Departure Airport": self._departure_airport,
            "Arrival Country": self._arrival_country,
            "Arrival Ariport": self._arrival_airport,
            "Price": str(self._price) + "Ft",
            "Departure date & time": self._departure_datetime.strftime("%Y-%m-%d %H:%M:%S")
        }

