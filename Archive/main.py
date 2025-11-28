from datetime import date
from Person import Client,Provider
from Service import Service
from Book import Booking



if __name__ == "__main__":

    omolola = Client("Omolola", "+48-881278182")
    tola = Provider("Tola", "+48-123456789", "test")

    bob = Client("Bob", "+47 888823232")

    service = Service("Haircut", 100, 5, omolola, tola)
    service2 = Service("Barber", 80, 90, bob, tola)

    booking_date = date(2023, 10, 1)
    time_slot = "10:00 AM - 11:00 AM"

    Omolola_booking = Booking(omolola, tola, service, booking_date, time_slot)
    # print(Omolola_booking.booking_confirmation())

    print(service.info())
    print(service2.info())