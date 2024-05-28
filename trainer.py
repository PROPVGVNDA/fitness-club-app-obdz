from models import Trainer
from mongoengine import DoesNotExist

def create_trainer():
    name = input("Enter trainer's name: ")
    specialty = input("Enter trainer's specialty: ")
    trainer = Trainer(name=name, specialty=specialty)
    trainer.save()
    print(f"Trainer {name} created successfully.")

def get_trainers():
    trainers = Trainer.objects()
    for trainer in trainers:
        print(trainer.to_json())

def get_trainer():
    trainer_id = input("Enter trainer's ID: ")
    try:
        trainer = Trainer.objects.get(id=trainer_id)
        print(trainer.to_json())
    except DoesNotExist:
        print(f"Trainer with ID {trainer_id} does not exist.")

def update_trainer():
    trainer_id = input("Enter trainer's ID: ")
    try:
        trainer = Trainer.objects.get(id=trainer_id)
        name = input(f"Enter new name (current: {trainer.name}): ") or trainer.name
        specialty = input(f"Enter new specialty (current: {trainer.specialty}): ") or trainer.specialty
        trainer.update(name=name, specialty=specialty)
        print(f"Trainer {trainer_id} updated successfully.")
    except DoesNotExist:
        print(f"Trainer with ID {trainer_id} does not exist.")

def delete_trainer():
    trainer_id = input("Enter trainer's ID: ")
    try:
        trainer = Trainer.objects.get(id=trainer_id)
        trainer.delete()
        print(f"Trainer {trainer_id} deleted successfully.")
    except DoesNotExist:
        print(f"Trainer with ID {trainer_id} does not exist.")
