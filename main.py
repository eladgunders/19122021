from datetime import datetime
from sqlalchemy import text
from db_config import local_session, create_all_entities
from DbRepo import DbRepo
from Flight import Flight
from Country import Country
from Ticket import Ticket
from Airline_Company import Airline_Company
from Customer import Customer
from User import User
from User_Role import User_Role
from Administrator import Administrator
import sys
from Kita import Kita
from Student import Student


repo = DbRepo(local_session)  # creating a 'DAO'

create_all_entities()  # create tables if not exist

# crerating 2 kitot
#kita1 = Kita(floor=1, num_of_students=30, class_avg=0)
#kita2 = Kita(floor=3, num_of_students=32, class_avg=0)
#repo.add_all([kita1, kita2])

# creating 3 students
#student1 = Student(fname='Elad', lname='Gunders', grade_avg='100', kita_id = 2)
#repo.add(student1)
#student2 = Student(fname='Uri', lname='Goldshmid', grade_avg='92', kita_id = 2)
#repo.add(student2)
#student3 = Student(fname='Itay', lname='Hauptman', grade_avg='98', kita_id = 1)
#repo.add(student3)
#student4 = Student(fname='Tomer', lname='Hermesh', grade_avg='96', kita_id = 1)
#repo.add(student4)

print(repo.get_by_column_value(Student, Student.kita_id, 1))
print(repo.get_by_column_value(Student, Student.kita_id, 2))


