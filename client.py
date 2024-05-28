from models import Client
from mongoengine import DoesNotExist

def create_client():
    name = input("Enter client's name: ")
    age = int(input("Enter client's age: "))
    memberships = list(map(int, input("Enter memberships (comma separated): ").split(',')))
    client = Client(name=name, age=age, memberships=memberships)
    client.save()
    print(f"Client {name} created successfully.")

def get_clients():
    clients = Client.objects()
    print(clients)
    for client in clients:
        print(client.to_json())

def get_client():
    client_id = input("Enter client's ID: ")
    try:
        client = Client.objects.get(id=client_id)
        print(client.to_json())
    except DoesNotExist:
        print(f"Client with ID {client_id} does not exist.")

def update_client():
    client_id = input("Enter client's ID: ")
    try:
        client = Client.objects.get(id=client_id)
        name = input(f"Enter new name (current: {client.name}): ") or client.name
        age = input(f"Enter new age (current: {client.age}): ") or client.age
        memberships = input(f"Enter new memberships (comma separated, current: {client.memberships}): ")
        memberships = list(map(int, memberships.split(','))) if memberships else client.memberships
        client.update(name=name, age=age, memberships=memberships)
        print(f"Client {client_id} updated successfully.")
    except DoesNotExist:
        print(f"Client with ID {client_id} does not exist.")

def delete_client():
    client_id = input("Enter client's ID: ")
    try:
        client = Client.objects.get(id=client_id)
        client.delete()
        print(f"Client {client_id} deleted successfully.")
    except DoesNotExist:
        print(f"Client with ID {client_id} does not exist.")
