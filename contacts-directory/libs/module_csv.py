import csv
import time
from typing import List, Dict, Any

FILE_CSV = "contacts.csv"

def convert_csv(data):
  data_formatter: List[Dict[str, str]] = []
  for row in data:
    if not row or row[0] == 'first_name':
      continue

    contact = {
      "first_name": "",
      "last_name": "",
      "phone_number": ""
    }
    
    for i in range(len(row)):
      col = row[i]
      col_name = ""

      if i == 0:
        col_name = "first_name"
      elif i == 1:
        col_name = "last_name"
      elif i == 2:
        col_name = "phone_number"
      else:
        col_name = "first_name"

      contact[col_name] = col

    data_formatter.append(contact)
  return data_formatter

def deconvert_csv(data: List[Dict[str, str]]) -> List[List[str]]:
  data_formatter: List[List[str]] = []
  data_formatter.append(["first_name", "last_name", "phone_number"])

  for row in data:
    contact = [row["first_name"], row["last_name"], row["phone_number"]]
    data_formatter.append(contact)

  return data_formatter

def list_contacts() -> List[Dict[str, str]]:
  with open(FILE_CSV, "r", encoding="utf-8") as file:
    csv_file = csv.reader(file, "excel", delimiter=",")
    data = convert_csv(csv_file)
    file.close()
  return data

def add_contact(new_contact: Dict[str, Any]):
  with open(FILE_CSV, "r", encoding="utf-8") as file:
    csv_file = csv.reader(file, "excel", delimiter=",")
    contacts = convert_csv(csv_file)

    for contact in contacts:
      if contact["first_name"] == new_contact["first_name"]:
        return

    contacts.append(new_contact)

  with open(FILE_CSV, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    contacts_formatter = deconvert_csv(contacts)
    for contact in contacts_formatter:
      writer.writerow(contact)

def delete_contact(first_name: str):
  with open(FILE_CSV, "r", encoding="utf-8") as file:
    csv_file = csv.reader(file, "excel", delimiter=",")
    contacts = convert_csv(csv_file)

  contacts = [c for c in contacts if c["first_name"] != first_name]

  with open(FILE_CSV, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    contacts_formatter = deconvert_csv(contacts)
    for contact in contacts_formatter:
      writer.writerow(contact)

def update_contact(first_name: str, data: Dict[str, Any]):
  with open(FILE_CSV, "r", encoding="utf-8") as file:
    csv_file = csv.reader(file, "excel", delimiter=",")
    contacts = convert_csv(csv_file)

  for i in range(len(contacts)):
    if type(data["first_name"]) == str and contacts[i]["first_name"] == data["first_name"]:
      return

    if contacts[i]["first_name"] == first_name:
      contacts[i] = data
      break

  with open(FILE_CSV, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    contacts_formatter = deconvert_csv(contacts)
    for contact in contacts_formatter:
      writer.writerow(contact)
