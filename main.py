import argparse
import os
from mongoengine import connect
from populate import run_population
from trainer import (
    create_trainer,
    get_trainers,
    get_trainer,
    update_trainer,
    delete_trainer
)
from client import (
    create_client,
    get_clients,
    get_client,
    update_client,
    delete_client
)
from membership import (
    create_membership,
    get_memberships,
    get_membership,
    update_membership,
    delete_membership
)
from class_module import (
    create_class,
    get_classes,
    get_class,
    update_class,
    delete_class
)
from record import (
    create_record,
    get_records,
    get_record,
    update_record,
    delete_record
)

def main():
    parser = argparse.ArgumentParser(description="Fitness Club Application")
    parser.add_argument("--populate", action="store_true", help="Populate MongoDB with sample data")
    args = parser.parse_args()

    mongo_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    connect(host=mongo_url)

    if args.populate:
        run_population()
        return

    while True:
        print("Choose model to work with:")
        print("1. Client")
        print("2. Trainer")
        print("3. Membership")
        print("4. Class")
        print("5. Record")
        print("0. Exit")
        model_choice = int(input("Enter choice: "))

        if model_choice == 0:
            break

        if model_choice == 1:
            print("Choose operation:")
            print("1. Get all clients")
            print("2. Get a client")
            print("3. Create a client")
            print("4. Update a client")
            print("5. Delete a client")
            operation_choice = int(input("Enter choice: "))

            if operation_choice == 1:
                get_clients()
            elif operation_choice == 2:
                get_client()
            elif operation_choice == 3:
                create_client()
            elif operation_choice == 4:
                update_client()
            elif operation_choice == 5:
                delete_client()
            else:
                print("Invalid choice")

        elif model_choice == 2:
            print("Choose operation:")
            print("1. Get all trainers")
            print("2. Get a trainer")
            print("3. Create a trainer")
            print("4. Update a trainer")
            print("5. Delete a trainer")
            operation_choice = int(input("Enter choice: "))

            if operation_choice == 1:
                get_trainers()
            elif operation_choice == 2:
                get_trainer()
            elif operation_choice == 3:
                create_trainer()
            elif operation_choice == 4:
                update_trainer()
            elif operation_choice == 5:
                delete_trainer()
            else:
                print("Invalid choice")

        elif model_choice == 3:
            print("Choose operation:")
            print("1. Get all memberships")
            print("2. Get a membership")
            print("3. Create a membership")
            print("4. Update a membership")
            print("5. Delete a membership")
            operation_choice = int(input("Enter choice: "))

            if operation_choice == 1:
                get_memberships()
            elif operation_choice == 2:
                get_membership()
            elif operation_choice == 3:
                create_membership()
            elif operation_choice == 4:
                update_membership()
            elif operation_choice == 5:
                delete_membership()
            else:
                print("Invalid choice")

        elif model_choice == 4:
            print("Choose operation:")
            print("1. Get all classes")
            print("2. Get a class")
            print("3. Create a class")
            print("4. Update a class")
            print("5. Delete a class")
            operation_choice = int(input("Enter choice: "))

            if operation_choice == 1:
                get_classes()
            elif operation_choice == 2:
                get_class()
            elif operation_choice == 3:
                create_class()
            elif operation_choice == 4:
                update_class()
            elif operation_choice == 5:
                delete_class()
            else:
                print("Invalid choice")

        elif model_choice == 5:
            print("Choose operation:")
            print("1. Get all records")
            print("2. Get a record")
            print("3. Create a record")
            print("4. Update a record")
            print("5. Delete a record")
            operation_choice = int(input("Enter choice: "))

            if operation_choice == 1:
                get_records()
            elif operation_choice == 2:
                get_record()
            elif operation_choice == 3:
                create_record()
            elif operation_choice == 4:
                update_record()
            elif operation_choice == 5:
                delete_record()
            else:
                print("Invalid choice")

        else:
            print("Invalid model choice")

if __name__ == "__main__":
    main()
