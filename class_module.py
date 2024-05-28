from models import Class, Trainer, Client
from mongoengine import DoesNotExist

def create_class():
    name = input("Enter class name: ")
    trainer_id = input("Enter trainer ID: ")
    try:
        trainer = Trainer.objects.get(id=trainer_id)
    except DoesNotExist:
        print(f"Trainer with ID {trainer_id} does not exist.")
        return
    client_ids = input("Enter client IDs (comma separated): ").split(',')
    clients = []
    for client_id in client_ids:
        try:
            client = Client.objects.get(id=client_id)
            clients.append(client)
        except DoesNotExist:
            print(f"Client with ID {client_id} does not exist.")
    class_ = Class(name=name, trainer=trainer, clients=clients)
    class_.save()
    print(f"Class {name} created successfully.")

def get_classes():
    classes = Class.objects()
    for class_ in classes:
        print(class_.to_json())

def get_class():
    class_id = input("Enter class's ID: ")
    try:
        class_ = Class.objects.get(id=class_id)
        print(class_.to_json())
    except DoesNotExist:
        print(f"Class with ID {class_id} does not exist.")

def update_class():
    class_id = input("Enter class's ID: ")
    try:
        class_ = Class.objects.get(id=class_id)
        name = input(f"Enter new name (current: {class_.name}): ") or class_.name
        trainer_id = input(f"Enter new trainer ID (current: {class_.trainer.id}): ") or class_.trainer.id
        try:
            trainer = Trainer.objects.get(id=trainer_id)
        except DoesNotExist:
            print(f"Trainer with ID {trainer_id} does not exist.")
            return
        client_ids = input(f"Enter new client IDs (comma separated, current: {[client.id for client in class_.clients]}): ")
        clients = []
        if client_ids:
            for client_id in client_ids.split(','):
                try:
                    client = Client.objects.get(id=client_id)
                    clients.append(client)
                except DoesNotExist:
                    print(f"Client with ID {client_id} does not exist.")
        else:
            clients = class_.clients
        class_.update(name=name, trainer=trainer, clients=clients)
        print(f"Class {class_id} updated successfully.")
    except DoesNotExist:
        print(f"Class with ID {class_id} does not exist.")

def delete_class():
    class_id = input("Enter class's ID: ")
    try:
        class_ = Class.objects.get(id=class_id)
        class_.delete()
        print(f"Class {class_id} deleted successfully.")
    except DoesNotExist:
        print(f"Class with ID {class_id} does not exist.")
