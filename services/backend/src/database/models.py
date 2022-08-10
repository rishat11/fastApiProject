from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from .database import Base


class Movie(Base):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256))
    description = Column(Text)
    screenings = relationship('Screening', back_populates='movie')


class Screening(Base):
    __tablename__ = 'screening'

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey('movie.id'))
    movie = relationship('Movie', back_populates='screenings')
    auditorium_id = Column(Integer, ForeignKey('auditorium.id'))
    auditorium = relationship('Auditorium', back_populates='screenings')
    screening_start = Column(DateTime, nullable=False)


class Auditorium(Base):
    __tablename__ = 'auditorium'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32))
    screenings = relationship('Screening', back_populates='auditorium')


class Seat(Base):
    __tablename__ = 'seat'

    id = Column(Integer, primary_key=True, index=True)
    row = Column(Integer)
    number = Column(Integer)
    auditorium_id = Column(Integer, ForeignKey('auditorium.id'))
    auditorium = relationship('Auditorium')


class SeatReserved(Base):
    __tablename__ = 'seat_reserved'

    id = Column(Integer, primary_key=True, index=True)
    seat_id = Column(Integer, ForeignKey('seat.id'))
    seat = relationship('Seat')
    reservation_id = Column(Integer, ForeignKey('reservation.id'))
    reservation = relationship('Reservation')
    screening_id = Column(Integer, ForeignKey('screening.id'))
    screening = relationship('Screening')


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32))
    password = Column(String(100))
    created_at = Column(DateTime, nullable=False)
    modified_at = Column(DateTime, nullable=False)


class Reservation(Base):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True, index=True)
    screening_id = Column(Integer, ForeignKey('screening.id'))
    screening = relationship('Screening')
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship('Employee')
    paid = Column(Boolean)
    active = Column(Boolean)


class TokenData(Base):
    __tablename__ = 'token_data'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32))


class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String(256))
