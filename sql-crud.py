from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a new class based object for Programmer

class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

#create a new instance of sessionmaker, then point to our engine (The database in question)
Session = sessionmaker(db)
#Opens an actual session by calling the Session subclass defined above.
session = Session()

base.metadata.create_all(db)

#creating records for the programmer table

ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL Language"
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American",
    famous_for = "Inventing the term Software Engineering"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famous_for = "Microsoft"
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "British",
    famous_for = "World Wide Web"
)

phil_dakin = Programmer(
    first_name = "Phil",
    last_name = "Dakin",
    gender = "M",
    nationality = "British",
    famous_for = "A series of tubes"
)

#Adding the record to the session
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(phil_dakin)
#committing the record to the database

# updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Being a madlad"

# #updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "M":
#         person.gender = "Male"
#     elif person.gender == "F":
#         person.gender = "Female"
#     else:
#         print("Gender not defined")
fname = input("Enter the first name of the programmer you want to delete: ")
lname = input("Enter the last name of the programmer you want to delete: ")
programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
if programmer is not None:
    print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this record? (y/n): ")
    if confirmation.lower() == "y":
        session.delete(programmer)
        print("Programmer deleted")
    else:
        print("Programmer not deleted")

else:
    print("Programmer not found")

session.commit()

programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
          programmer.first_name + " " + programmer.last_name,
          programmer.gender,
          programmer.nationality,
          programmer.famous_for,
          sep = " | "
          )

