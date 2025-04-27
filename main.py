from Airline import Airline
from DomesticFlight import DomesticFlight
from InternationalFlight import InternationalFlight
from Ticket import Ticket
from datetime import datetime
import os

class BookSystem:
    def __init__(self):
        self.airlines: Airline = []
        self.tickets: Ticket = []
        self._init_data()

    def add_airline(self, airline: Airline):
        self.airlines.append(airline)

    def display_airlines(self):
        for airline in self.airlines:
            print(f"Airline Name: {airline.name}, Code: {airline.code}")
            airline.print_flights()
            
    def _init_data(self):
        airline1 = Airline("Budapest Airline", "BPS")

        domestic_flight1 = DomesticFlight("BPS111", "BUD", "PEC",  200.0, datetime.strptime("2023-10-01 10:00", "%Y-%m-%d %H:%M"), "Budapest", "Pécs")
        domestic_flight2 = DomesticFlight("BPS222", "BUD", "DEB",  300.0, datetime.strptime("2023-10-01 11:00", "%Y-%m-%d %H:%M"), "Budapest", "Debrecen")
        international_flight1 = InternationalFlight("BPS333", "BUD", "BER", 800.0, datetime.strptime("2023-10-01 12:00", "%Y-%m-%d %H:%M"), "Hungary", "Germany")
        international_flight2 = InternationalFlight("BPS444", "BUD", "LIS", 1200.0, datetime.strptime("2023-10-01 13:00", "%Y-%m-%d %H:%M"), "Hungary", "Portugal")

        airline1.add_flight(domestic_flight1)
        airline1.add_flight(domestic_flight2)
        airline1.add_flight(international_flight1)
        airline1.add_flight(international_flight2)

        self.add_airline(airline1)
        self.display_airlines()
    
    def find_flight_by_number(self, flight_number: str):
        for airline in self.airlines:
            for flight in airline.flights:
                if flight.flight_number == flight_number:
                    return flight
        return None
    
    def book_ticket(self):
        flight_number = input("Enter flight number: ")
        flight = self.find_flight_by_number(flight_number)
        if flight:
            ticket_id = len(self.tickets) + 1
            passenger_name = input("Enter passenger name: ")
            ticket = Ticket(ticket_id, passenger_name, flight)
            self.tickets.append(ticket)
            print(f"Ticket booked successfully! Ticket ID: {ticket_id}")
        else:
            print("Flight not found.")
    
    def list_tickets(self):
        if not self.tickets:
            print("No tickets booked.")
            return False
        for ticket in self.tickets:
            print(f"Ticket ID: {ticket._ticket_id}, Passenger Name: {ticket._passenger_name}, Flight Number: {ticket._flight.flight_number}")
        return True
    
    def cancel_ticket(self):
        try:
            ticket_id = int(input("Enter ticket ID to cancel: "))
        except ValueError:
            print("Invalid input. Please enter a valid ticket ID.")
            return

        for ticket in self.tickets:
            if ticket._ticket_id == ticket_id:
                self.tickets.remove(ticket)
                print(f"Ticket ID {ticket_id} cancelled successfully.")
                return

        print("Ticket not found. Please enter a valid ticket ID.")
        
    def user_interface(self):
        while True:
            print("\n1. List flights")
            print("2. Book a ticket")
            print("3. List tickets")
            print("4. Cancel a ticket")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                clear_console()
                self.display_airlines()
            elif choice == '2':
                clear_console()
                self.display_airlines()
                self.book_ticket()
            elif choice == '3':
                clear_console()
                self.list_tickets()
            elif choice == '4':
                clear_console()
                if self.list_tickets(): 
                    self.cancel_ticket()
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
        
clear_console()
bookSystem = BookSystem()
bookSystem.user_interface()