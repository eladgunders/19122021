from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, REAL, BigInteger, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship, backref
from db_config import Base


class Student(Base):
    __tablename__ = 'students'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    fname = Column(String(15), nullable=False)
    lname = Column(String(25), nullable=False)
    grade_avg = Column(REAL(), nullable=False)
    kita_id = Column(BigInteger(), ForeignKey('kita.id'), unique=False, nullable=False)

    __table_args__ = (UniqueConstraint('fname', 'lname', name='una_1'),)

    kita = relationship("Kita", backref=backref("students", uselist=True))

    def __repr__(self):
        return f'<Student> id={self.id}, fname={self.fname}, lname={self.lname}, grade_avg={self.grade_avg}, ' \
               f'kita_id={self.kita_id}    kita = {self.kita}'

    def __str__(self):
        return f'<Student> id={self.id}, fname={self.fname}, lname={self.lname}, grade_avg={self.grade_avg}, ' \
               f'kita_id={self.kita_id}    kita = {self.kita}'


