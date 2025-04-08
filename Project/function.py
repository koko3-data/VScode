
import datetime
import json
from os import remove
import pandas as pd

def add_producers():
    producers ={}
    counter = 1
    

    producer_identity = input("Enter producer_name (prod_name1,prod_name2): ").lower().split(",")
    producer_identity = [identity.strip() for identity in producer_identity]
    for identity in producer_identity:
        producer_name = identity.split(",")
        prod_prefix = identity[:3].upper()
        key_id = f"{prod_prefix}-PROD-{counter}-{int(datetime.datetime.now().timestamp())}"
        counter += 1
       

        services = {}
        category_services ={
            "hair":[],
            "makeup":[],
            "afro_dishes":[],
            "african_shops":[],
            "others":[]}
        producer_service = input(f"Services provided by {producer_name}: ").split(",")
        producer_service = [service.strip() for service in producer_service]
        for item in producer_service:
            try:
                service_price = float(input(f"Enter price for {item}: "))
                services[item] = service_price
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
                for service,price in services.items():
                    asked_category = input(f"Enter the category for {item}: ")
                    if asked_category == "hair":
                        category_services["hair"].append(service)
                    elif asked_category== "makeup":
                        category_services["makeup"].append(service)
                    elif asked_category == "afro_dishes":
                        category_services["afro_dishes"].append(service)
                    elif asked_category == "african_shops":
                        category_services["african_shops"].append(service)
                    elif asked_category == "others":
                        category_services["others"].append(service)

        producer_location = input(f"Address of {producer_name}: ")
        producer_social_media = input(f"Social media of {producer_name}: ")
        try:
            producer_contact = int(input(f"Contact of {producer_name}: "))
        except ValueError:
            print("Invalid contact. Please enter a numeric value.")
        producer_email = input(f"Email of {producer_name}: ")

        producer_description = {"location": producer_location,
                                 "social_media": producer_social_media, 
                                 "contact": producer_contact, 
                                 "email": producer_email
                                 }
        

       
        producers[key_id] = {
            "name": producer_name,
            "category_services": services,
            "information": producer_description
        }
    return producers



def save(producers):
    try:
        with open("producers.json", "r") as file:
            existing_producer_file = json.load(file)
            
    except FileNotFoundError:
        existing_producer_file = {}
        print("File does not exist. Creating a new file.")  
#Aviod duplicates by checking through producer_name
    for key_id, producer_data in producers.items():
        producer_name = producer_data["name"]
        if any(existing["name"] == producer_name for existing in existing_producer_file.values()):
            print(f"Duplicate producer found :{producer_name}")
            print("Select an option:")
            print("1. Skip the new entry")
            print("2. Delete the existing entry and add the new one")
            print("3. Add the new entry without deleting the existing one")
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1" :
             print(f"Duplicate producer {producer_name} skipped.")
            elif choice == "2" :
             for key,existing in list(existing_producer_file.items()):
                 if existing["name"] == producer_name:
                     del existing_producer_file[key]
                     print(f"Duplicate producer {producer_name} dropped from existing_file")
            elif choice == "3" :
             existing_producer_file[key_id] = producer_data
             print(f"New Producer with existing name - {producer_name} added to existing_file")
            else:
                print("Invalid choice. Please select a valid option.")
                continue
        else:
             existing_producer_file[key_id] = producer_data
 
    with open("producers.json", "w") as file:
        json.dump(existing_producer_file, file, indent=4)
        
    print("Data saved successfully.")
    producer_update = producers
    return producer_update


def add_service(producer_saved):
    #to add or update producer_service
    producer_name = input("Enter the producer name to update: ")
    for key_id, producer_data in producer_saved.items():
        if producer_data == ["name"]:
            producer_service = input(f"Enter the new service(s) provided by {producer_name}: ").split(",")
            producer_service = [service.strip() for service in producer_service]
            for service in producer_service:
                try:
                    service_price = float(input(f"Enter price for {service}: "))
                    producer_saved[producer_name]["services"][service] = service_price
                except ValueError:
                    print("Invalid price. Please enter a numeric value.")
            return producer_saved
        else:
            print("Producer not found.")
            return producer_saved
    
def delete_service(producer_saved):
    producer_name = input("Enter the producer name to delete service: ")
    if producer_name in producer_saved:
        #    for services in existing_producer_data[producer_name]["services"]:
        #         print(services)
        for index, service in enumerate(producer_saved[producer_name]["services"]):
            print(f"{index}: {service}")
            service_index = int(input("Enter the index of the service to delete: "))
            if service_index >= 0 and service_index < len(producer_saved[producer_name]["services"]):
                deleted_service = producer_saved[producer_name]["services"].pop(service_index)
                print(f"Deleted service: {deleted_service}")
                print(f"Updated services {producer_name}: {producer_saved[producer_name]['services']}")
                return producer_saved
                

def display_list(producer_saved):
    for key,id, producer in producer_saved.items():
       producer_table = pd.DataFrame.from_dict(producer, orient="index")
       print("Producers Table")
       return producer_table
    
def menu():
    producer_saved = {}
    
    
    
    while True:
        print('\033[1;34m' + "Welcome to your selection interface" + '\033[0m')
        print('\033[1;36m'+ "1. Add producers" + '\033[0m')
        print('\033[1;36m'+ "2. Add service" + '\033[0m')
        print('\033[1;36m'+ "3. Delete service" + '\033[0m')
        print('\033[1;36m'+ "4. Display producers" + '\033[0m')
        print('\033[1;36m'+ "5. Exit" + '\033[0m')



        choice = input("Enter your choice: ")
        if choice == "1":
            producers_data = add_producers()
            producer_saved = save(producers_data)
            print('\033[1;32m' + "Yippy! You have successfully added producers." + '\033[0m')

        elif choice == "2":
            update_service = add_service(producer_saved)
            producer_saved = save(update_service)
            print('\033[1;32m' + "Yippy! You have successfully updated service." + '\033[0m')
        
        elif choice == "3":
            delete_service = delete_service(producer_saved)
            producer_saved = save(delete_service)
            print('\033[1;32m' + "Yippy! You have successfully deleted service." + '\033[0m')

        elif choice == "4":
            display_producer = display_list(producer_saved)
            print(display_producer)
            print('\033[1;32m' + "Yippy! You have successfully displayed producers." + '\033[0m')

        elif choice == "5":
            print('\033[1;32m' + "Thank you for using the application." + '\033[0m')
            break
        
        else:
            print('\033[1;31m' + "Enter a valid." + '\033[0m')
            
        
        
    
   



   
