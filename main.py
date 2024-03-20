import pandas as pd


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id, "name"].squeeze()

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
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation
        Here is your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}"""

        return content


df = pd.read_csv("hotel.csv")
print(df)
hotel_ID = int(input("Enter the id of Hotel: "))
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())

else:
    print("Hotel is not free.")

