from mongoengine import Document, StringField, IntField, EmailField, StringField

class Student(Document):
    name = StringField(required=True, max_length=100)
    roll_number = StringField(required=True, unique=True, max_length=20)
    age = IntField(required=True)
    email = EmailField(required=True, unique=True)
    phone_number = StringField(required=True, max_length=15)

    def __str__(self):
        return f'<Student {self.name}, Roll Number: {self.roll_number}>'
