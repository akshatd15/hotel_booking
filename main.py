import pandas as pd

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        pass
    def book(self):
        """Books a hotel by changing its availability"""
        df.loc[df['id'] == self.hotel_id, "available"] = "no"
        df.to_csv('hotel.csv', index=False)

    def available(self):
        """Checks if the hotel is avaialble"""
        availability = df.loc[df['id'] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True

        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass
    def generate(self):
        pass


df = pd.read_csv("hotels.csv")
print(df)
hotel_ID = int(input("Enter the id of Hotel: "))
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    reservation_ticket.generate()

else:
    print("Hotel is not free.")

