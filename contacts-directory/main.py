import time
import os
import libs.module_csv as csv
import libs.module_json as json
TYPE_FILE = "json"

options = ("Add contact", "Modify contact", "Delete contact", "Exit")
options_to_modify = {
  1: "first_name",
  2: "last_name",
  3: "phone_number"
}

while True:
  try:
    print("Hello! This is the contact list.")

    contacts = []
    if TYPE_FILE == "json": contacts = json.list_contacts()  
    elif TYPE_FILE == "csv": contacts = csv.list_contacts()  
    else: contacts = csv.list_contacts()  
    
    if len(contacts) >= 0:
      for i in range(len(contacts)):
        contact = contacts[i]
        first_name = str(contact["first_name"]).capitalize()
        last_name = str(contact["last_name"]).capitalize()
        phone_number = contact["phone_number"]
        
        print(f"{i + 1}. {last_name} {first_name}: +{phone_number}")
        if i == len(contacts) -1:
          print(f"{'-'*50}\n")
        # else:
        #   print()
    else:
      print("Your contact directory is empty!!\n")

    # break
    for i in range(len(options)):
      option = options[i]
      print(f"{i + 1}. {option}")
    
    option = int(input("What do you want to do now? "))
    if type(option) != int or option == 4:
      break
    
    if option == 1:
      first_name = input("What would be the first name? ")
      last_name = input("What would be the last name? ")
      phone_number = input("What is the phone number? ")
      
      new_contact = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number
      }

      if TYPE_FILE == "json": json.add_contact(new_contact)
      elif TYPE_FILE == "csv": csv.add_contact(new_contact)
    elif option == 2:
      first_name_contact = input("Which contact do you want to modify? (provide first name) ")
      selected_contact = {}

      for contact in contacts:
          if contact["first_name"] != first_name_contact:
              continue
          selected_contact = contact
          break

      if not selected_contact:
          print("Contact not found.")
          break

      options_to_modify = {
          1: "first_name",
          2: "last_name",
          3: "phone_number"
      }

      print()
      for i in range(1, len(options_to_modify) + 1):
          print(f"{i}. {options_to_modify[i]}")
      print(f"{'-'*50}\n")

      option_to_modify = int(input("Choose what you want to modify: "))

      if option_to_modify not in options_to_modify:
          print("Invalid option.")
          break

      new_value = input("Enter new value: ")
      selected_contact[options_to_modify[option_to_modify]] = new_value

      if TYPE_FILE == "json": json.update_contact(first_name_contact, selected_contact)
      elif TYPE_FILE == "csv": csv.update_contact(first_name_contact, selected_contact)
    elif option == 3:
      first_name_contact = input("Which contact do you want to dle? (provide first name) ")

      if TYPE_FILE == "json": json.delete_contact(first_name_contact)
      elif TYPE_FILE == "csv": csv.delete_contact(first_name_contact)

    time.sleep(5)
    os.system('cls' if os.name == 'nt' else 'clear')

  except:
    # print(Errpr)
    break
