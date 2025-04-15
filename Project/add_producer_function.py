import re
import uuid
# from view_tags_function import tags
import json
import os



def add_producers():
    if not os.path.exists("producers.json"):
        with open("producers.json", "w") as file:
            json.dump({}, file)

    with open("producers.json", "r") as file:
        producers = json.load(file)

    
    

    producers_name = input("Enter producers name (producer_1, producer_2): ").lower().split(",")
    producers_name = [name.strip() for name in producers_name]

    #to generate producer_id
    for name in producers_name:
        producer_prefix = name[:2].upper()
        producer_id = f"{producer_prefix} - {uuid.uuid4().hex[:7].upper()}" 

    #to give producer service description
        producer_description = input(f"Enter {name} service description: ")

    # to add producer location
        producer_location = input(f"Enter {name} location: ")

    #to add producer social media
        instagram ={}
        facebook = {}
        twitter = {}
        tiktok = {}

        instagram = input(f"Enter {name} for producer instagram: ").split(",")
        instagram = [name.strip() for name in instagram]
        facebook = input(f"Enter {name} for producer facebook: ").split(",")
        facebook = [name.strip() for name in facebook]
        twitter = input(f"Enter {name} for producer twitter: ").split(",")
        twitter = [name.strip() for name in twitter]
        tiktok = input(f"Enter {name} for producer tiktok: ").split(",")
        tiktok = [name.strip() for name in tiktok]

        producer_social_media = {
            "instagram": instagram,
            "facebook": facebook,
            "twitter": twitter,
            "tiktok": tiktok
        }

        #to add producer email
        producers_email = input(f"Enter {name} email: ").lower().split(",")
    

        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        valid_email = [email.strip() for email in producers_email if re.match(email_regex, email.strip())]
        producers_email = valid_email
        if not valid_email:
            producers_email = []
            
        #to add producer contact
        producers_contact = input(f"Enter {name} contact: ").split(",")

        phone_regex = r'^\+?\d{1,3}[\s-]?\d{6,12}$'

        valid_contact = [contact.strip() for contact in producers_contact if re.match(phone_regex, contact.strip())]
        producers_contact = valid_contact
        if not valid_contact:
            producers_contact = []

        
        #to add producers services
        services = {}
        producers_service = input(f"Enter services provided by {name}(comma-seperated):").lower().split(",")
        producers_service = [service.strip() for service in producers_service]
        for service in producers_service:
            options ={}
            ask_option = input(f"Does {service} include options or not (yes/no): ").lower().strip()
            if ask_option == "no":
                try:
                    service_cost = float(input(f"Enter cost for {service}: "))
                    services[service] = service_cost
                except ValueError:
                    print(f"Invalid cost for {service}. Please enter a numeric value.")
            elif ask_option == "yes":
                options = input(f"Enter options for {service} (men,women,medium,long,short)(comma-separated): ").lower().split(",")
                options = [option.strip() for option in options]
                for option in options:
                    service_desc = service + " " + option

                    try:
                        service_cost = float(input(f"Enter cost for {service_desc}: "))
                        services[service_desc] = service_cost
                    except ValueError:
                        print(f"Invalid cost for {service}. Please enter a numeric value.")
                
      

                

    producers[producer_id] = {
            "name": name,
            "description": producer_description,
            "location": producer_location,
            "social_media": producer_social_media,
            "email": producers_email,
            "contact": producers_contact,
            "service": services
        }
 

    with open("producers.json", "w") as file:
        json.dump(producers, file, indent=4)

    return producers
   
    
    
    

    





    

    


