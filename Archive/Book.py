from datetime import date
from time import time
from Person import Client,Provider
from Service import Service



class Booking:
    def __init__ (self, client : Client , provider :Provider,service: Service,booking_date:date,time_slot:time):
        self.client = client
        self.provider = provider
        self.service = service
        self.booking_date = booking_date
        self.time_slot = time_slot
     
    
    def total_price(self):
        return self.service.price_quote()
    
    def booking_confirmation(self):
        return(
            f"\n Booking confirmation\n"
            f"Client :  {self.client.name}\n"
            f"Provider :  {self.provider.name}\n"
            f"Date : {self.booking_date}\n"
            f"Time : {self.time_slot}\n"
            f"Service: {self.service.name}\n"
            f"Total Price: {self.total_price()} PLN."
    
        )