from models import Trainer, Client, Membership, Class, Record

def run_population():
    trainers = [
        Trainer(name="John Doe", specialty="Cardio").save(),
        Trainer(name="Jane Smith", specialty="Yoga").save()
    ]
    
    clients = [
        Client(name="Alice", age=28, memberships=[1]).save(),
        Client(name="Bob", age=35, memberships=[2]).save(),
        Client(name="Jack", age=17, memberships=[2]).save()
    ]
    
    memberships = [
        Membership(type="Monthly", price=50).save(),
        Membership(type="Annual", price=500).save()
    ]
    
    classes = [
        Class(name="Morning Yoga", trainer=trainers[1], clients=[clients[0]]).save(),
        Class(name="Evening Cardio", trainer=trainers[0], clients=[clients[1]]).save(),
        Class(name="Weights", trainer=trainers[0], clients=[clients[0], clients[1]]).save()
    ]
    
    records = [
        Record(client=clients[0], class_id=classes[0], date="2024-05-01").save(),
        Record(client=clients[1], class_id=classes[1], date="2024-05-02").save()
    ]

    print("Test data population completed.")
