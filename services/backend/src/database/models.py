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


class Seat(Base):
    __tablename__ = 'seat'

    id = Column(Integer, primary_key=True, index=True)
    row = Column(Integer)
    number = Column(Integer)
    auditorium_id = Column(Integer, ForeignKey('auditorium.id'))
    auditorium = relationship('Auditorium', back_populates='seats')


class SeatReserved(Base):
    __tablename__ = 'seat_reserved'

    id = Column(Integer, primary_key=True, index=True)
    seat_id = Column(Integer, ForeignKey('seat.id'))
    seat = relationship('Seat', back_populates='seats_reserved')
    reservation_id = Column(Integer, ForeignKey('reservation.id'))
    reservation = relationship('Reservation', back_populates='seats_reserved')
    screening_id = Column(Integer, ForeignKey('screening.id'))
    screening = relationship('Screening', back_populates='seats_reserved')


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
    screening = relationship('Screening', back_populates='reservations')
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship('Employee', back_populates='reservations')
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
