from models import Record, Client, Class
from mongoengine import DoesNotExist

def create_record():
    client_id = input("Enter client ID: ")
    class_id = input("Enter class ID: ")
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        client = Client.objects.get(id=client_id)
    except DoesNotExist:
        print(f"Client with ID {client_id} does not exist.")
        return
    try:
        class_ = Class.objects.get(id=class_id)
    except DoesNotExist:
        print(f"Class with ID {class_id} does not exist.")
        return
    record = Record(client=client, class_id=class_, date=date)
    record.save()
    print("Record created successfully.")

def get_records():
    records = Record.objects()
    for record in records:
        print(record.to_json())

def get_record():
    record_id = input("Enter record's ID: ")
    try:
        record = Record.objects.get(id=record_id)
        print(record.to_json())
    except DoesNotExist:
        print(f"Record with ID {record_id} does not exist.")

def update_record():
    record_id = input("Enter record's ID: ")
    try:
        record = Record.objects.get(id=record_id)
        client_id = input(f"Enter new client ID (current: {record.client.id}): ") or record.client.id
        class_id = input(f"Enter new class ID (current: {record.class_id.id}): ") or record.class_id.id
        date = input(f"Enter new date (current: {record.date}): ") or record.date
        try:
            client = Client.objects.get(id=client_id)
        except DoesNotExist:
            print(f"Client with ID {client_id} does not exist.")
            return
        try:
            class_ = Class.objects.get(id=class_id)
        except DoesNotExist:
            print(f"Class with ID {class_id} does not exist.")
            return
        record.update(client=client, class_id=class_, date=date)
        print(f"Record {record_id} updated successfully.")
    except DoesNotExist:
        print(f"Record with ID {record_id} does not exist.")

def delete_record():
    record_id = input("Enter record's ID: ")
    try:
        record = Record.objects.get(id=record_id)
        record.delete()
        print(f"Record {record_id} deleted successfully.")
    except DoesNotExist:
        print(f"Record with ID {record_id} does not exist.")
