flights = {
    "AI101": {"source": "Delhi", "dest": "Mumbai", "seats": 5, "price": 5500},
    "AI102": {"source": "Mumbai", "dest": "Delhi", "seats": 8, "price": 5200},
    "6E201": {"source": "Bangalore", "dest": "Chennai", "seats": 3, "price": 3200},
    "6E202": {"source": "Chennai", "dest": "Bangalore", "seats": 4, "price": 3100}
}


def book_flight():

    source = input("Enter Source City: ")
    destination = input("Enter Destination City: ")

    for flight_no, details in flights.items():

        if details["source"].lower() == source.lower() and details["dest"].lower() == destination.lower():

            print("\nFlight Available")
            print("Flight Number:", flight_no)
            print("Available Seats:", details["seats"])
            print("Price:", details["price"])

            seats = int(input("How many seats do you want to book? "))

            if seats <= details["seats"]:

                details["seats"] = details["seats"] - seats

                print("\nBooking Confirmed")
                print("Booked Seats:", seats)
                print("Remaining Seats:", details["seats"])

            else:
                print("Not enough seats available")

            return

    print("No Flight Available")


book_flight()
