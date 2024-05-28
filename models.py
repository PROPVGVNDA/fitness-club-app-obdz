from mongoengine import Document, StringField, IntField, ListField, ReferenceField

class Trainer(Document):
    name = StringField(required=True)
    specialty = StringField(required=True)

class Client(Document):
    name = StringField(required=True)
    age = IntField(required=True)
    memberships = ListField(IntField(), required=True)

class Membership(Document):
    type = StringField(required=True)
    price = IntField(required=True)

class Class(Document):
    name = StringField(required=True)
    trainer = ReferenceField(Trainer)
    clients = ListField(ReferenceField(Client))

class Record(Document):
    client = ReferenceField(Client)
    class_id = ReferenceField(Class)
    date = StringField(required=True)
