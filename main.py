import argparse
import os
from pymongo import MongoClient
from populate import run_population

def main():
    parser = argparse.ArgumentParser(description="Fitness Club Application")
    parser.add_argument("--populate", action="store_true", help="Populate MongoDB with sample data")
    args = parser.parse_args()

    mongo_url = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    client = MongoClient(mongo_url)

    if args.populate:
        run_population(client)
    else:
        db = client.fitness_club
        print("Information about classes and their trainers:")
        pipeline = [
            {
                "$lookup": {
                    "from": "trainers",
                    "localField": "trainer_id",
                    "foreignField": "_id",
                    "as": "trainer_info"
                }
            }
        ]
        trainers_and_classes = list(db.classes.aggregate(pipeline))
        for t in trainers_and_classes:
            print(t)
        print("-" * 70)
        print("List of clients who have membership of type 2:")
        clients = db.clients.find({"memberships": 2})
        for client in clients:
            print(client)
        

if __name__ == "__main__":
    main()
