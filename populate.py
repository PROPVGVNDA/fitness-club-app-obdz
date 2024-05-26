from pymongo import MongoClient

def run_population(client):
    db = client.fitness_club
    
    trainers = [
        {"_id": 1, "name": "John Doe", "specialty": "Cardio"},
        {"_id": 2, "name": "Jane Smith", "specialty": "Yoga"}
    ]
    
    clients = [
        {"_id": 1, "name": "Alice", "age": 28, "memberships": [1]},
        {"_id": 2, "name": "Bob", "age": 35, "memberships": [2]},
        {"_id": 3, "name": "Jack", "age": 17, "memberships": [2]}
    ]
    
    memberships = [
        {"_id": 1, "type": "Monthly", "price": 50},
        {"_id": 2, "type": "Annual", "price": 500}
    ]
    
    classes = [
        {"_id": 1, "name": "Morning Yoga", "trainer_id": 2, "clients": [1]},
        {"_id": 2, "name": "Evening Cardio", "trainer_id": 1, "clients": [2]},
        {"_id": 3, "name": "Weights", "trainer_id": 1, "clients": [1, 2]}
    ]
    
    records = [
        {"_id": 1, "client_id": 1, "class_id": 1, "date": "2024-05-01"},
        {"_id": 2, "client_id": 2, "class_id": 2, "date": "2024-05-02"}
    ]

    db.trainers.insert_many(trainers)
    db.clients.insert_many(clients)
    db.memberships.insert_many(memberships)
    db.classes.insert_many(classes)
    db.records.insert_many(records)
    
    print("Test data population completed.")
