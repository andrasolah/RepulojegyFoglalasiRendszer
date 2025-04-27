from datetime import datetime
from Flight import Flight

class Ticket:
    def __init__(self, ticket_id: int, passenger_name: str, flight: Flight):
        self._ticket_id = ticket_id
        self._passenger_name = passenger_name
        self._flight = flight

