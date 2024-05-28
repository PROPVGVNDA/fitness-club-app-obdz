from models import Membership
from mongoengine import DoesNotExist

def create_membership():
    type = input("Enter membership type: ")
    price = int(input("Enter membership price: "))
    membership = Membership(type=type, price=price)
    membership.save()
    print(f"Membership {type} created successfully.")

def get_memberships():
    memberships = Membership.objects()
    for membership in memberships:
        print(membership.to_json())

def get_membership():
    membership_id = input("Enter membership's ID: ")
    try:
        membership = Membership.objects.get(id=membership_id)
        print(membership.to_json())
    except DoesNotExist:
        print(f"Membership with ID {membership_id} does not exist.")

def update_membership():
    membership_id = input("Enter membership's ID: ")
    try:
        membership = Membership.objects.get(id=membership_id)
        type = input(f"Enter new type (current: {membership.type}): ") or membership.type
        price = input(f"Enter new price (current: {membership.price}): ") or membership.price
        membership.update(type=type, price=price)
        print(f"Membership {membership_id} updated successfully.")
    except DoesNotExist:
        print(f"Membership with ID {membership_id} does not exist.")

def delete_membership():
    membership_id = input("Enter membership's ID: ")
    try:
        membership = Membership.objects.get(id=membership_id)
        membership.delete()
        print(f"Membership {membership_id} deleted successfully.")
    except DoesNotExist:
        print(f"Membership with ID {membership_id} does not exist.")
