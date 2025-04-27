from abc import ABC, abstractmethod
from datetime import datetime

class Flight(ABC):
    def __init__(self, flight_number: str, departure_airport: str, arrival_airport: str,  price: float, departure_datetime: datetime):
        self._flight_number = flight_number
        self._departure_airport = departure_airport
        self._arrival_airport = arrival_airport
        self._price = price
        self._departure_datetime = departure_datetime
    
    @abstractmethod
    def book_flight(self):
        pass
    
    @abstractmethod
    def cancel_flight(self):
        pass
    
    @abstractmethod
    def get_flight_details(self):
        pass
    
