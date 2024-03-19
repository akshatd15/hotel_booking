import pandas as pd

class Hotel:
    def __init__(self, id):
        pass
    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
    def generate(self):
        pass


df = pd.read_csv("hotels.csv")
print(df)
id = int(input("Enter the id of Hotel: "))
hotel = Hotel(id)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    reservation_ticket.generate()

else:
    print("Hotel is not free.")

