from Airline import Airline
from DomesticFlight import DomesticFlight
from InternationalFlight import InternationalFlight
from Ticket import Ticket
from datetime import datetime
import os
import shutil

class BookSystem:
    def __init__(self):
        self.airlines: Airline = []
        self.tickets: Ticket = []
        self._init_data()

    def add_airline(self, airline: Airline):
        self.airlines.append(airline)

    def display_airlines(self, formatted: bool = False):
        for airline in self.airlines:
            print(f"Airline Name: {airline.name}, Code: {airline.code}")
            airline.print_flights(formatted)
            
    def _init_data(self):
        airline1 = Airline("Budapest Airline", "BPS")

        domestic_flight1 = DomesticFlight("BPS111", "BUD", "PEC",  20000, datetime.strptime("2025-4-27 10:00", "%Y-%m-%d %H:%M"), "Budapest", "Pécs")
        domestic_flight2 = DomesticFlight("BPS222", "BUD", "DEB",  30000, datetime.strptime("2025-5-31 11:00", "%Y-%m-%d %H:%M"), "Budapest", "Debrecen")
        international_flight1 = InternationalFlight("BPS333", "BUD", "BER", 80000, datetime.strptime("2025-5-5 12:00", "%Y-%m-%d %H:%M"), "Hungary", "Germany")
        international_flight2 = InternationalFlight("BPS444", "BUD", "LIS", 120000, datetime.strptime("2025-6-10 13:00", "%Y-%m-%d %H:%M"), "Hungary", "Portugal")

        airline1.add_flight(domestic_flight1)
        airline1.add_flight(domestic_flight2)
        airline1.add_flight(international_flight1)
        airline1.add_flight(international_flight2)

        self.add_airline(airline1)
        
        self.book_ticket("Kiss Mária", "BPS111")
        self.book_ticket("Fekete András", "BPS222")
        self.book_ticket("Fekete András", "BPS333")
        self.book_ticket("Varga Zsófia", "BPS444")
        self.book_ticket("Szűcs Petra", "BPS222")
        self.book_ticket("Papp Gergely", "BPS444")
        
        self.display_airlines(True)
    
    def find_flight_by_number(self, flight_number: str):
        for airline in self.airlines:
            for flight in airline.flights:
                if flight.flight_number == flight_number:
                    return flight
        return None
    
    def book_ticket_manually(self):
        flight_number = input("Enter flight number: ")
        flight = self.find_flight_by_number(flight_number)
        if flight:
            if flight.departure_datetime < datetime.now():
                print("Cannot book a ticket for a flight that has already departed.")
                return
            ticket_id = len(self.tickets) + 1
            while True:
                passenger_name = input("Enter passenger name (or 'exit' to cancel): ").strip()
                if passenger_name.lower() == "exit":
                    return
                if not passenger_name:
                    print("Passenger name cannot be empty. Please try again.")
                    continue
                break
            ticket = Ticket(ticket_id, passenger_name, flight)
            self.tickets.append(ticket)
            print(f"Ticket booked successfully! Ticket ID: {ticket_id}")
        else:
            print("Flight not found.")
    
    def book_ticket(self,passenger_name=None,flight_number=None):
        if passenger_name and flight_number:
            ticket_id = len(self.tickets) + 1
            ticket = Ticket(ticket_id, passenger_name, self.find_flight_by_number(flight_number))
            self.tickets.append(ticket)
        else:
            self.book_ticket_manually()
    
    def list_tickets(self):
        if not self.tickets:
            print("No tickets booked.")
            return False
        print(f"{'Ticket ID':<10} {'Passenger Name':<20} {'Flight Number':<15} {'Price (Ft)':<15} {'Destination':<15} {'Flight Date & Time':<20}")
        print("-" * 100)
        for ticket in self.tickets:
            print(f"{ticket.ticket_id:<10} {ticket.passenger_name:<20} {ticket.flight.flight_number:<15} {ticket.flight.price:<15} {ticket.flight.get_destination():<15} {ticket.flight.departure_datetime.strftime('%Y-%m-%d %H:%M:%S'):<20}")
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
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    clear_console()
                    self.display_airlines(True)
                elif choice == 2:
                    clear_console()
                    self.display_airlines(True)
                    self.book_ticket()
                elif choice == 3:
                    clear_console()
                    self.list_tickets()
                elif choice == 4:
                    clear_console()
                    if self.list_tickets(): 
                        self.cancel_ticket()
                elif choice == 5:
                    break
                else:
                    clear_console()
                    self.display_airlines(True)
                    print("Invalid choice. Please try again.")
            except ValueError:
                clear_console()
                self.display_airlines(True)
                print("Invalid input. Please enter a valid input.")
    
    def set_console_width(width: int, height: int = 25):
    if os.name == "nt":
        os.system(f"mode con: cols={width} lines={height}")
    else:
        os.system(f"printf '\033[8;{height};{width}t'")

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
        



bookSystem = BookSystem()
bookSystem.set_console_width(150, 30)
clear_console()
bookSystem.user_interface()