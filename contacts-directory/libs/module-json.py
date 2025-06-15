import json
from typing import List, Dict, Any

FILE_JSON = "contacts.json"

def list_contacts():
  with open(FILE_JSON, "r", encoding="utf-8") as file:
    contacts: List[Dict[str, Any]] = json.load(file)
    return contacts

def add_contact(new_contact: Dict[str, Any]):
  with open(FILE_JSON, "r", encoding="utf-8") as file:
    contacts: List[Dict[str, Any]] = json.load(file)

  for contact in contacts:
    if contact["first_name"] == new_contact["first_name"]:
      return

  contacts.append(new_contact)
  with open(FILE_JSON, "w", encoding="utf-8") as file:
    json.dump(contacts, file, indent=2)

def delete_contact(first_name: str):
  with open(FILE_JSON, "r", encoding="utf-8") as file:
    contacts: List[Dict[str, Any]] = json.load(file)

  contacts = [c for c in contacts if c["first_name"] != first_name]

  with open(FILE_JSON, "w", encoding="utf-8") as file:
    json.dump(contacts, file, indent=2)

def update_contact(first_name: str, data: Dict[str, Any]):
  with open(FILE_JSON, "r", encoding="utf-8") as file:
    contacts: List[Dict[str, Any]] = json.load(file)

  for i in range(len(contacts)):
    if contacts[i]["first_name"] == first_name:
      contacts[i] = data
      break

  with open(FILE_JSON, "w", encoding="utf-8") as file:
    json.dump(contacts, file, indent=2)
