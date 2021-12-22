from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, REAL, BigInteger
from sqlalchemy.orm import relationship
from db_config import Base


class Kita(Base):
    __tablename__ = 'kita'

    id = Column(BigInteger(), primary_key=True, autoincrement=True)
    floor = Column(Integer(), nullable=False)
    num_of_students = Column(Integer(), nullable=False)
    class_avg = Column(REAL(), nullable=False)

    def __repr__(self):
        return f'<Kita> id={self.id}, floor={self.floor}, num_of_students={self.num_of_students}, class_avg={self.class_avg}'

    def __str__(self):
        return f'<Kita> id={self.id}, floor={self.floor}, num_of_students={self.num_of_students}, class_avg={self.class_avg}'

